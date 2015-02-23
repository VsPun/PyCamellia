%module (package = "PyCamellia") TimeRamp
%{
#include "Function.h"
#include "ParameterFunction.h"

class TimeRamp : public SimpleFunction {
  FunctionPtr _time;
  double _timeScale;
  double getTimeValue() {
    ParameterFunction* timeParamFxn = dynamic_cast<ParameterFunction*>(_time.get());
    SimpleFunction* timeFxn = dynamic_cast<SimpleFunction*>(timeParamFxn->getValue().get());
    return timeFxn->value(0);
  }
public:
  TimeRamp(FunctionPtr timeConstantParamFxn, double timeScale) {
    _time = timeConstantParamFxn;
    _timeScale = timeScale;
  }
  double value(double x) {
    double t = getTimeValue();
    if (t >= _timeScale) {
      return 1.0;
    } else {
      return t / _timeScale;
    }
  }
  static FunctionPtr timeRamp(FunctionPtr timeConstantParamFxn, double timeScale=1.0) {
    return Teuchos::rcp( new TimeRamp(timeConstantParamFxn, timeScale) );
  }
};
%}

%include "Camellia.i"

%nodefaultctor TimeRamp;

class TimeRamp {
public:
  static FunctionPtr timeRamp(FunctionPtr timeConstantParamFxn, double timeScale=1.0);
};
