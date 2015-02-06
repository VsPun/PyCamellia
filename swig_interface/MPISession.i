%module MPISession
%{
#include "Teuchos_GlobalMPISession.hpp"
#include "Teuchos_RCP.hpp"
class MPISession {
  Teuchos::RCP<Teuchos::GlobalMPISession> _mpiSession;
public:
  MPISession() {
    int argc = 0;
    char** argv = {NULL};
    _mpiSession = Teuchos::rcp( new Teuchos::GlobalMPISession(&argc,&argv) );
  }
};
%}

class MPISession {
public:
  MPISession();
};
