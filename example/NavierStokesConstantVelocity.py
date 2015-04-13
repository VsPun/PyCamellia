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
polyOrder = 3
delta_k = 1

form = NavierStokesVGPFormulation(meshTopo,Re,polyOrder,delta_k)

form.addZeroMeanPressureCondition()

inflow1 = SpatialFilter.matchingX(0.0)
inflow2 = SpatialFilter.matchingX(8.0)
outflow = SpatialFilter.matchingY(0.0) or SpatialFilter.matchingY(2.0)

y = Function.yn(1)
inflowVelocity_x = Function.constant(1.0)
inflowVelocity_y = Function.constant(0.0)
inflowVelocity = Function.vectorize(inflowVelocity_x,inflowVelocity_y)

form.addOutflowCondition(outflow)
form.addInflowCondition(inflow1,inflowVelocity)
form.addInflowCondition(inflow2,inflowVelocity)

refinementNumber = 0

nonlinearThreshold = 1e-3

#define a local method that will do the nonlinear iteration:
def nonlinearSolve(maxSteps):
  normOfIncrement = 1
  stepNumber = 0
  while normOfIncrement > nonlinearThreshold and stepNumber < maxSteps:
    form.solveAndAccumulate()
    normOfIncrement = form.L2NormSolutionIncrement()
    print("L^2 norm of increment: %0.3f" % normOfIncrement)
    stepNumber += 1

maxSteps = 10
nonlinearSolve(maxSteps)
mesh = form.solution().mesh();

energyError = form.solutionIncrement().energyErrorTotal()
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
