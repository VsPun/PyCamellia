from PyCamellia import *
spaceDim = 2
useConformingTraces = False
form = StokesVGPFormulation(spaceDim,useConformingTraces)
dims = [1.0,1.0]
numElements = [2,2]
x0 = [0.,0.]
meshTopo = MeshFactory.rectilinearMeshTopology(dims,numElements,x0)
polyOrder = 2
delta_k = 1

form.initializeSolution(meshTopo,polyOrder,delta_k)

form.addZeroMeanPressureCondition()

topBoundary = SpatialFilter.matchingY(1.0)
notTopBoundary = not topBoundary

one = Function.constant(1.0)
zero = Function.constant(0.0)
topVelocity = Function.vectorize(one,zero)

form.addWallCondition(notTopBoundary)
form.addInflowCondition(topBoundary,topVelocity)

form.solve()

energyError = form.solution().energyErrorTotal()
print(energyError)
