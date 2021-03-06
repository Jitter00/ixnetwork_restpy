# Copyright 1997 - 2018 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PassCriteria(Base):
	"""The PassCriteria class encapsulates a required passCriteria node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the PassCriteria property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'passCriteria'

	def __init__(self, parent):
		super(PassCriteria, self).__init__(parent)

	@property
	def DataErrorThresholdMode(self):
		"""The data error calculated for the threshold mode.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('dataErrorThresholdMode')
	@DataErrorThresholdMode.setter
	def DataErrorThresholdMode(self, value):
		self._set_attribute('dataErrorThresholdMode', value)

	@property
	def DataErrorThresholdValue(self):
		"""The integer value for the threshold data error.

		Returns:
			number
		"""
		return self._get_attribute('dataErrorThresholdValue')
	@DataErrorThresholdValue.setter
	def DataErrorThresholdValue(self, value):
		self._set_attribute('dataErrorThresholdValue', value)

	@property
	def EnableDataIntegrityPassFail(self):
		"""If true, the data integrity pass /fail criteria is set.

		Returns:
			bool
		"""
		return self._get_attribute('enableDataIntegrityPassFail')
	@EnableDataIntegrityPassFail.setter
	def EnableDataIntegrityPassFail(self, value):
		self._set_attribute('enableDataIntegrityPassFail', value)

	@property
	def EnableLatencyPassFail(self):
		"""If true, the latency pass fail criteria is set.

		Returns:
			bool
		"""
		return self._get_attribute('enableLatencyPassFail')
	@EnableLatencyPassFail.setter
	def EnableLatencyPassFail(self, value):
		self._set_attribute('enableLatencyPassFail', value)

	@property
	def EnablePassFail(self):
		"""If true, the pass fail criteria is set.

		Returns:
			bool
		"""
		return self._get_attribute('enablePassFail')
	@EnablePassFail.setter
	def EnablePassFail(self, value):
		self._set_attribute('enablePassFail', value)

	@property
	def EnableRatePassFail(self):
		"""If true, the rate of pass and fail criteria is set.

		Returns:
			bool
		"""
		return self._get_attribute('enableRatePassFail')
	@EnableRatePassFail.setter
	def EnableRatePassFail(self, value):
		self._set_attribute('enableRatePassFail', value)

	@property
	def EnableSequenceErrorsPassFail(self):
		"""If true, the sequence errors for the pass and fail criteria is set.

		Returns:
			bool
		"""
		return self._get_attribute('enableSequenceErrorsPassFail')
	@EnableSequenceErrorsPassFail.setter
	def EnableSequenceErrorsPassFail(self, value):
		self._set_attribute('enableSequenceErrorsPassFail', value)

	@property
	def EnableStandardDeviationPassFail(self):
		"""If true, Standard Deviation for the Pass/Fail criteria is set.

		Returns:
			bool
		"""
		return self._get_attribute('enableStandardDeviationPassFail')
	@EnableStandardDeviationPassFail.setter
	def EnableStandardDeviationPassFail(self, value):
		self._set_attribute('enableStandardDeviationPassFail', value)

	@property
	def LatencyThresholdMode(self):
		"""The threshold mode for the latency.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('latencyThresholdMode')
	@LatencyThresholdMode.setter
	def LatencyThresholdMode(self, value):
		self._set_attribute('latencyThresholdMode', value)

	@property
	def LatencyThresholdScale(self):
		"""The scale by which the latency threshold is measured.

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('latencyThresholdScale')
	@LatencyThresholdScale.setter
	def LatencyThresholdScale(self, value):
		self._set_attribute('latencyThresholdScale', value)

	@property
	def LatencyThresholdValue(self):
		"""The value by which legacy threshold value is to be measured.

		Returns:
			number
		"""
		return self._get_attribute('latencyThresholdValue')
	@LatencyThresholdValue.setter
	def LatencyThresholdValue(self, value):
		self._set_attribute('latencyThresholdValue', value)

	@property
	def LatencyVarThresholdMode(self):
		"""The latency variation threshold mode.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('latencyVarThresholdMode')
	@LatencyVarThresholdMode.setter
	def LatencyVarThresholdMode(self, value):
		self._set_attribute('latencyVarThresholdMode', value)

	@property
	def LatencyVariationThresholdScale(self):
		"""The scale by which the latency variation threshold is measured.

		Returns:
			str(ms|ns|us)
		"""
		return self._get_attribute('latencyVariationThresholdScale')
	@LatencyVariationThresholdScale.setter
	def LatencyVariationThresholdScale(self, value):
		self._set_attribute('latencyVariationThresholdScale', value)

	@property
	def LatencyVariationThresholdValue(self):
		"""The value by which the variation in latency threshold is measured.

		Returns:
			number
		"""
		return self._get_attribute('latencyVariationThresholdValue')
	@LatencyVariationThresholdValue.setter
	def LatencyVariationThresholdValue(self, value):
		self._set_attribute('latencyVariationThresholdValue', value)

	@property
	def PassCriteriaLoadRateMode(self):
		"""The downstream traffic pass criteria for load rate mode.

		Returns:
			str(average|minimum)
		"""
		return self._get_attribute('passCriteriaLoadRateMode')
	@PassCriteriaLoadRateMode.setter
	def PassCriteriaLoadRateMode(self, value):
		self._set_attribute('passCriteriaLoadRateMode', value)

	@property
	def PassCriteriaLoadRateScale(self):
		"""The pass criteria scale in which the load rate is to be measured.

		Returns:
			str(fps|gbps|kbps|mbps|percent)
		"""
		return self._get_attribute('passCriteriaLoadRateScale')
	@PassCriteriaLoadRateScale.setter
	def PassCriteriaLoadRateScale(self, value):
		self._set_attribute('passCriteriaLoadRateScale', value)

	@property
	def PassCriteriaLoadRateValue(self):
		"""The pass criteria for the Value of the load rate.

		Returns:
			number
		"""
		return self._get_attribute('passCriteriaLoadRateValue')
	@PassCriteriaLoadRateValue.setter
	def PassCriteriaLoadRateValue(self, value):
		self._set_attribute('passCriteriaLoadRateValue', value)

	@property
	def PassFailFrequency(self):
		"""NOT DEFINED

		Returns:
			str(framesizes|trials)
		"""
		return self._get_attribute('passFailFrequency')
	@PassFailFrequency.setter
	def PassFailFrequency(self, value):
		self._set_attribute('passFailFrequency', value)

	@property
	def SeqErrorsThresholdMode(self):
		"""The recorded sequence error in the threshold mode.

		Returns:
			str(average|maximum)
		"""
		return self._get_attribute('seqErrorsThresholdMode')
	@SeqErrorsThresholdMode.setter
	def SeqErrorsThresholdMode(self, value):
		self._set_attribute('seqErrorsThresholdMode', value)

	@property
	def SeqErrorsThresholdValue(self):
		"""The threshold value of the sequence errors.

		Returns:
			number
		"""
		return self._get_attribute('seqErrorsThresholdValue')
	@SeqErrorsThresholdValue.setter
	def SeqErrorsThresholdValue(self, value):
		self._set_attribute('seqErrorsThresholdValue', value)

	def Apply(self):
		"""Executes the apply operation on the server.

		Applies the specified Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('apply', payload=payload, response_object=None)

	def ApplyAsync(self):
		"""Executes the applyAsync operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyAsync', payload=payload, response_object=None)

	def ApplyAsyncResult(self):
		"""Executes the applyAsyncResult operation on the server.

			Returns:
				bool: 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyAsyncResult', payload=payload, response_object=None)

	def ApplyITWizardConfiguration(self):
		"""Executes the applyITWizardConfiguration operation on the server.

		Applies the specified Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

	def GenerateReport(self):
		"""Executes the generateReport operation on the server.

		Generate a PDF report for the last succesfull test run.

			Returns:
				str: This method is asynchronous and has no return value.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('generateReport', payload=payload, response_object=None)

	def Run(self, *args, **kwargs):
		"""Executes the run operation on the server.

		Starts the specified Quick Test and waits for its execution to finish.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		run()list

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		run(InputParameters:string)list
			Args:
				args[0] is InputParameters (str): The input arguments of the test.

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('run', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Starts the specified Quick Test.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(InputParameters:string)
			Args:
				args[0] is InputParameters (str): The input arguments of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stops the currently running Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)

	def WaitForTest(self):
		"""Executes the waitForTest operation on the server.

		Waits for the execution of the specified Quick Test to be completed.

			Returns:
				list(str): This method is synchronous and returns the result of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('waitForTest', payload=payload, response_object=None)
