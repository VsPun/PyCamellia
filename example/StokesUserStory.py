import matplotlib.pyplot as plt
import numpy as np
import sys

from PyCamellia import *
spaceDim = 2
Re = 800.0
dims = [8.0,2.0]
numElements = [8,2]
x0 = [0.,0.]
meshTopo = MeshFactory.rectilinearMeshTopology(dims,numElements,x0)
polyOrder = 2
delta_k = 1
spaceDim = 2

useConformingTraces = False
form = StokesVGPFormulation(spaceDim, useConformingTraces)
form.initializeSolution(meshTopo,polyOrder,delta_k)
form.addZeroMeanPressureCondition()

inflow = SpatialFilter.matchingX(0.0) & SpatialFilter.greaterThanY(1.0)
outflow = SpatialFilter.matchingX(8.0)
wall = SpatialFilter.negatedFilter(inflow | outflow)

#test the filters:
wallPoints = [[0,0.5],[6,0],[8,0],[0.1,2],[7.9,2]]
wallOK = True
for point in wallPoints:
  if not wall.matchesPoint(point):
    print "Error--wall does not match point " + str(point)
    wallOK = False
  if inflow.matchesPoint(point):
    print "Error--inflow matches wall point " + str(point)
  if outflow.matchesPoint(point):
    print "Error--outflow matches wall point " + str(point)  

y = Function.yn(1)
inflowVelocity_x = -3*(y-1)*(y-2)
inflowVelocity_y = Function.constant(0.0)
inflowVelocity = Function.vectorize(inflowVelocity_x,inflowVelocity_y)

form.addWallCondition(wall)
form.addOutflowCondition(outflow)
form.addInflowCondition(inflow,inflowVelocity)

refinementNumber = 0
form.solve()

energyError = form.solution().energyErrorTotal()
mesh = form.solution().mesh()
elementCount = mesh.numActiveElements()
globalDofCount = mesh.numGlobalDofs()
print("Initial mesh has %i elements and %i degrees of freedom." % (elementCount, globalDofCount))
print("Energy error after %i refinements: %0.3f" % (refinementNumber, energyError))

u1_soln = Function.solution(form.u(1),form.solution())

num_x = 10
num_y = 10
refCellVertexPoints = []

for j in range(num_y):
  y = -1 + 2. * float(j) / float(num_y - 1) # go from -1 to 1
  for i in range(num_x):
    x = -1 + 2. * float(i) / float(num_x - 1) # go from -1 to 1
    refCellVertexPoints.append([x,y])

zList = [] # should have tuples (zVals, (x_min,x_max), (y_min,y_max)) -- one for each cell
activeCellIDs = mesh.getActiveCellIDs()
xMin = sys.float_info.max
xMax = sys.float_info.min
yMin = sys.float_info.max
yMax = sys.float_info.min
zMin = sys.float_info.max
zMax = sys.float_info.min
for cellID in activeCellIDs:
  vertices = mesh.verticesForCell(cellID)
  xMinLocal = vertices[0][0]
  xMaxLocal = vertices[1][0]
  yMinLocal = vertices[0][1]
  yMaxLocal = vertices[2][1]
  (values,points) = u1_soln.getCellValues(mesh,cellID,refCellVertexPoints)
  zValues = np.array(values) 
  zValues = zValues.reshape((num_x,num_y)) # 2D array
  zMin = min(zValues.min(),zMin)
  zMax = max(zValues.max(),zMax)
  zList.append((zValues,(xMinLocal,xMaxLocal),(yMinLocal,yMaxLocal)))
  xMin = min(xMinLocal,xMin)
  xMax = max(xMaxLocal,xMax)
  yMin = min(yMinLocal,yMin)
  yMax = max(yMaxLocal,yMax)

if abs(zMax - zMin) < 1e-3:
  zMax = zMin + 1.0

#plot them
for zTuple in zList:
  zValues,(xMinLocal,xMaxLocal),(yMinLocal,yMaxLocal) = zTuple
  plt.imshow(zValues, cmap='coolwarm', vmin=zMin, vmax=zMax,
           extent=[xMinLocal, xMaxLocal, yMinLocal, yMaxLocal],
           interpolation='bicubic', origin='lower')

plt.title('constant flow u_1')
plt.colorbar()
plt.axis([xMin, xMax, yMin, yMax])
plt.show()
