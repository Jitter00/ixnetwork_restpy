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


class TestConfig(Base):
	"""The TestConfig class encapsulates a required testConfig node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the TestConfig property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'testConfig'

	def __init__(self, parent):
		super(TestConfig, self).__init__(parent)

	@property
	def BinaryBackoff(self):
		"""The percentage to be applied to the search interval through which the next iterations rate is obtained.

		Returns:
			number
		"""
		return self._get_attribute('binaryBackoff')
	@BinaryBackoff.setter
	def BinaryBackoff(self, value):
		self._set_attribute('binaryBackoff', value)

	@property
	def BinaryFrameLossUnit(self):
		"""The binary frame loss unit.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('binaryFrameLossUnit')
	@BinaryFrameLossUnit.setter
	def BinaryFrameLossUnit(self, value):
		self._set_attribute('binaryFrameLossUnit', value)

	@property
	def BinaryLoadUnit(self):
		"""The binary load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('binaryLoadUnit')
	@BinaryLoadUnit.setter
	def BinaryLoadUnit(self, value):
		self._set_attribute('binaryLoadUnit', value)

	@property
	def BinaryResolution(self):
		"""The resolution of the iteration during a binary search.

		Returns:
			number
		"""
		return self._get_attribute('binaryResolution')
	@BinaryResolution.setter
	def BinaryResolution(self, value):
		self._set_attribute('binaryResolution', value)

	@property
	def BinarySearchType(self):
		"""The binary search type.

		Returns:
			str(linear|perFlow|perPort)
		"""
		return self._get_attribute('binarySearchType')
	@BinarySearchType.setter
	def BinarySearchType(self, value):
		self._set_attribute('binarySearchType', value)

	@property
	def BinaryTolerance(self):
		"""The percentage of frame loss that is acceptable in order for an iteration to be considered successful during a binary search.

		Returns:
			number
		"""
		return self._get_attribute('binaryTolerance')
	@BinaryTolerance.setter
	def BinaryTolerance(self, value):
		self._set_attribute('binaryTolerance', value)

	@property
	def BurstSize(self):
		"""It signifies the burst size of the protocol.

		Returns:
			number
		"""
		return self._get_attribute('burstSize')
	@BurstSize.setter
	def BurstSize(self, value):
		self._set_attribute('burstSize', value)

	@property
	def CalculateJitter(self):
		"""If true, enables jitter calculation.

		Returns:
			bool
		"""
		return self._get_attribute('calculateJitter')
	@CalculateJitter.setter
	def CalculateJitter(self, value):
		self._set_attribute('calculateJitter', value)

	@property
	def CalculateLatency(self):
		"""If true, enables latency calculation.

		Returns:
			bool
		"""
		return self._get_attribute('calculateLatency')
	@CalculateLatency.setter
	def CalculateLatency(self, value):
		self._set_attribute('calculateLatency', value)

	@property
	def ComboBackoff(self):
		"""The percentage to be applied to the search interval through which the next iterations rate is obtained, for Combo Load Type.

		Returns:
			number
		"""
		return self._get_attribute('comboBackoff')
	@ComboBackoff.setter
	def ComboBackoff(self, value):
		self._set_attribute('comboBackoff', value)

	@property
	def ComboFrameLossUnit(self):
		"""The combo frame loss unit.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('comboFrameLossUnit')
	@ComboFrameLossUnit.setter
	def ComboFrameLossUnit(self, value):
		self._set_attribute('comboFrameLossUnit', value)

	@property
	def ComboLoadUnit(self):
		"""The combo Load Unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('comboLoadUnit')
	@ComboLoadUnit.setter
	def ComboLoadUnit(self, value):
		self._set_attribute('comboLoadUnit', value)

	@property
	def ComboResolution(self):
		"""The resolution of the iteration for Combo Load Type.

		Returns:
			number
		"""
		return self._get_attribute('comboResolution')
	@ComboResolution.setter
	def ComboResolution(self, value):
		self._set_attribute('comboResolution', value)

	@property
	def ComboTolerance(self):
		"""The value of the tolerance level for Combo Load Type.

		Returns:
			number
		"""
		return self._get_attribute('comboTolerance')
	@ComboTolerance.setter
	def ComboTolerance(self, value):
		self._set_attribute('comboTolerance', value)

	@property
	def CountRandomFrameSize(self):
		"""If true, randomly counts the frame size.

		Returns:
			number
		"""
		return self._get_attribute('countRandomFrameSize')
	@CountRandomFrameSize.setter
	def CountRandomFrameSize(self, value):
		self._set_attribute('countRandomFrameSize', value)

	@property
	def CustomLoadUnit(self):
		"""The custom load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('customLoadUnit')
	@CustomLoadUnit.setter
	def CustomLoadUnit(self, value):
		self._set_attribute('customLoadUnit', value)

	@property
	def DelayAfterTransmit(self):
		"""Specifies the amount of delay after every transmit.

		Returns:
			number
		"""
		return self._get_attribute('delayAfterTransmit')
	@DelayAfterTransmit.setter
	def DelayAfterTransmit(self, value):
		self._set_attribute('delayAfterTransmit', value)

	@property
	def DetailedResultsEnabled(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('detailedResultsEnabled')
	@DetailedResultsEnabled.setter
	def DetailedResultsEnabled(self, value):
		self._set_attribute('detailedResultsEnabled', value)

	@property
	def Duration(self):
		"""The duration of the test in hours, which is used to calculate the number of framesto transmit.

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def EnableDataIntegrity(self):
		"""If true, enables data integrity test.

		Returns:
			bool
		"""
		return self._get_attribute('enableDataIntegrity')
	@EnableDataIntegrity.setter
	def EnableDataIntegrity(self, value):
		self._set_attribute('enableDataIntegrity', value)

	@property
	def EnableExtraIterations(self):
		"""If true, enables the tracking option in aggregation files.

		Returns:
			bool
		"""
		return self._get_attribute('enableExtraIterations')
	@EnableExtraIterations.setter
	def EnableExtraIterations(self, value):
		self._set_attribute('enableExtraIterations', value)

	@property
	def EnableFastConvergence(self):
		"""If true, enables fast convergence.

		Returns:
			bool
		"""
		return self._get_attribute('enableFastConvergence')
	@EnableFastConvergence.setter
	def EnableFastConvergence(self, value):
		self._set_attribute('enableFastConvergence', value)

	@property
	def EnableLayer1Rate(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableLayer1Rate')
	@EnableLayer1Rate.setter
	def EnableLayer1Rate(self, value):
		self._set_attribute('enableLayer1Rate', value)

	@property
	def EnableMinFrameSize(self):
		"""If true, enables minimum frame size.

		Returns:
			bool
		"""
		return self._get_attribute('enableMinFrameSize')
	@EnableMinFrameSize.setter
	def EnableMinFrameSize(self, value):
		self._set_attribute('enableMinFrameSize', value)

	@property
	def EnableOldStatsForReef(self):
		"""Enables old statistics for reef.

		Returns:
			bool
		"""
		return self._get_attribute('enableOldStatsForReef')
	@EnableOldStatsForReef.setter
	def EnableOldStatsForReef(self, value):
		self._set_attribute('enableOldStatsForReef', value)

	@property
	def ExtraIterationOffsets(self):
		"""Sets extra iteration offset values.

		Returns:
			str
		"""
		return self._get_attribute('extraIterationOffsets')
	@ExtraIterationOffsets.setter
	def ExtraIterationOffsets(self, value):
		self._set_attribute('extraIterationOffsets', value)

	@property
	def FastConvergenceDuration(self):
		"""sec

		Returns:
			number
		"""
		return self._get_attribute('fastConvergenceDuration')
	@FastConvergenceDuration.setter
	def FastConvergenceDuration(self, value):
		self._set_attribute('fastConvergenceDuration', value)

	@property
	def FastConvergenceThreshold(self):
		"""If true, enables fast convergence threshold value.

		Returns:
			number
		"""
		return self._get_attribute('fastConvergenceThreshold')
	@FastConvergenceThreshold.setter
	def FastConvergenceThreshold(self, value):
		self._set_attribute('fastConvergenceThreshold', value)

	@property
	def ForceRegenerate(self):
		"""Initiates a forced regeneration.

		Returns:
			bool
		"""
		return self._get_attribute('forceRegenerate')
	@ForceRegenerate.setter
	def ForceRegenerate(self, value):
		self._set_attribute('forceRegenerate', value)

	@property
	def FrameLossUnit(self):
		"""The frame loss unit.

		Returns:
			str
		"""
		return self._get_attribute('frameLossUnit')
	@FrameLossUnit.setter
	def FrameLossUnit(self, value):
		self._set_attribute('frameLossUnit', value)

	@property
	def FrameOrderingByRfc2889(self):
		"""If true, indicates frame ordering by Rfc2889.

		Returns:
			bool
		"""
		return self._get_attribute('frameOrderingByRfc2889')
	@FrameOrderingByRfc2889.setter
	def FrameOrderingByRfc2889(self, value):
		self._set_attribute('frameOrderingByRfc2889', value)

	@property
	def FrameSizeMode(self):
		"""This attribute is the frame size mode for the Quad Gaussian.

		Returns:
			str(custom|customlist|increment|random)
		"""
		return self._get_attribute('frameSizeMode')
	@FrameSizeMode.setter
	def FrameSizeMode(self, value):
		self._set_attribute('frameSizeMode', value)

	@property
	def FramesPerBurstGap(self):
		"""It signifies the frames per burst gap.

		Returns:
			number
		"""
		return self._get_attribute('framesPerBurstGap')
	@FramesPerBurstGap.setter
	def FramesPerBurstGap(self, value):
		self._set_attribute('framesPerBurstGap', value)

	@property
	def Framesize(self):
		"""Bytes

		Returns:
			number
		"""
		return self._get_attribute('framesize')
	@Framesize.setter
	def Framesize(self, value):
		self._set_attribute('framesize', value)

	@property
	def FramesizeList(self):
		"""List containing the frame sizes used in the test.

		Returns:
			list(str)
		"""
		return self._get_attribute('framesizeList')
	@FramesizeList.setter
	def FramesizeList(self, value):
		self._set_attribute('framesizeList', value)

	@property
	def Gap(self):
		"""Inter-frame gap.

		Returns:
			number
		"""
		return self._get_attribute('gap')
	@Gap.setter
	def Gap(self, value):
		self._set_attribute('gap', value)

	@property
	def GenerateTrackingOptionAggregationFiles(self):
		"""If true, enables the tracking option in aggregation files.

		Returns:
			bool
		"""
		return self._get_attribute('generateTrackingOptionAggregationFiles')
	@GenerateTrackingOptionAggregationFiles.setter
	def GenerateTrackingOptionAggregationFiles(self, value):
		self._set_attribute('generateTrackingOptionAggregationFiles', value)

	@property
	def InitialBinaryLoadRate(self):
		"""The load rate used in the first iteration for each frame size during a binary search.

		Returns:
			number
		"""
		return self._get_attribute('initialBinaryLoadRate')
	@InitialBinaryLoadRate.setter
	def InitialBinaryLoadRate(self, value):
		self._set_attribute('initialBinaryLoadRate', value)

	@property
	def InitialComboLoadRate(self):
		"""The initial value of the load rate for Combo Load Type.

		Returns:
			number
		"""
		return self._get_attribute('initialComboLoadRate')
	@InitialComboLoadRate.setter
	def InitialComboLoadRate(self, value):
		self._set_attribute('initialComboLoadRate', value)

	@property
	def InitialStepLoadRate(self):
		"""The initial value of the load rate for Step Load Type.

		Returns:
			number
		"""
		return self._get_attribute('initialStepLoadRate')
	@InitialStepLoadRate.setter
	def InitialStepLoadRate(self, value):
		self._set_attribute('initialStepLoadRate', value)

	@property
	def LatencyBins(self):
		"""Sets the latency bins statistics

		Returns:
			str
		"""
		return self._get_attribute('latencyBins')
	@LatencyBins.setter
	def LatencyBins(self, value):
		self._set_attribute('latencyBins', value)

	@property
	def LatencyBinsEnabled(self):
		"""Enables the latency bins statistics

		Returns:
			bool
		"""
		return self._get_attribute('latencyBinsEnabled')
	@LatencyBinsEnabled.setter
	def LatencyBinsEnabled(self, value):
		self._set_attribute('latencyBinsEnabled', value)

	@property
	def LatencyType(self):
		"""The type of latency.

		Returns:
			str(cutThrough|storeForward)
		"""
		return self._get_attribute('latencyType')
	@LatencyType.setter
	def LatencyType(self, value):
		self._set_attribute('latencyType', value)

	@property
	def LoadRateList(self):
		"""The list of Load Rate.

		Returns:
			str
		"""
		return self._get_attribute('loadRateList')
	@LoadRateList.setter
	def LoadRateList(self, value):
		self._set_attribute('loadRateList', value)

	@property
	def LoadType(self):
		"""The type of load.

		Returns:
			str(binary|combo|custom|quickSearch|step|unchanged)
		"""
		return self._get_attribute('loadType')
	@LoadType.setter
	def LoadType(self, value):
		self._set_attribute('loadType', value)

	@property
	def MapType(self):
		"""The POS traffic map type.

		Returns:
			str
		"""
		return self._get_attribute('mapType')
	@MapType.setter
	def MapType(self, value):
		self._set_attribute('mapType', value)

	@property
	def MaxBinaryLoadRate(self):
		"""The lower bound of the iteration rates for each frame size during a binary search.

		Returns:
			number
		"""
		return self._get_attribute('maxBinaryLoadRate')
	@MaxBinaryLoadRate.setter
	def MaxBinaryLoadRate(self, value):
		self._set_attribute('maxBinaryLoadRate', value)

	@property
	def MaxComboLoadRate(self):
		"""The maximum value of the load rate Combo Load Type.

		Returns:
			number
		"""
		return self._get_attribute('maxComboLoadRate')
	@MaxComboLoadRate.setter
	def MaxComboLoadRate(self, value):
		self._set_attribute('maxComboLoadRate', value)

	@property
	def MaxIncrementFrameSize(self):
		"""The maximum incremental value of the frame size.

		Returns:
			number
		"""
		return self._get_attribute('maxIncrementFrameSize')
	@MaxIncrementFrameSize.setter
	def MaxIncrementFrameSize(self, value):
		self._set_attribute('maxIncrementFrameSize', value)

	@property
	def MaxQuickSearchLoadRate(self):
		"""Sets the maximum QuickSearch load rate

		Returns:
			number
		"""
		return self._get_attribute('maxQuickSearchLoadRate')
	@MaxQuickSearchLoadRate.setter
	def MaxQuickSearchLoadRate(self, value):
		self._set_attribute('maxQuickSearchLoadRate', value)

	@property
	def MaxRandomFrameSize(self):
		"""The maximum random frame size to be sent.

		Returns:
			number
		"""
		return self._get_attribute('maxRandomFrameSize')
	@MaxRandomFrameSize.setter
	def MaxRandomFrameSize(self, value):
		self._set_attribute('maxRandomFrameSize', value)

	@property
	def MaxStepLoadRate(self):
		"""The maximum value of the load rate Step Load Type.

		Returns:
			number
		"""
		return self._get_attribute('maxStepLoadRate')
	@MaxStepLoadRate.setter
	def MaxStepLoadRate(self, value):
		self._set_attribute('maxStepLoadRate', value)

	@property
	def MinBinaryLoadRate(self):
		"""The lower bound of the iteration rates for each frame size during a binary search.

		Returns:
			number
		"""
		return self._get_attribute('minBinaryLoadRate')
	@MinBinaryLoadRate.setter
	def MinBinaryLoadRate(self, value):
		self._set_attribute('minBinaryLoadRate', value)

	@property
	def MinComboLoadRate(self):
		"""The minimum value of the load rate Combo Load Type.

		Returns:
			number
		"""
		return self._get_attribute('minComboLoadRate')
	@MinComboLoadRate.setter
	def MinComboLoadRate(self, value):
		self._set_attribute('minComboLoadRate', value)

	@property
	def MinFpsRate(self):
		"""The rate at which minimum frames are sent per second.

		Returns:
			number
		"""
		return self._get_attribute('minFpsRate')
	@MinFpsRate.setter
	def MinFpsRate(self, value):
		self._set_attribute('minFpsRate', value)

	@property
	def MinIncrementFrameSize(self):
		"""The minimum incremental value of the frame size.

		Returns:
			number
		"""
		return self._get_attribute('minIncrementFrameSize')
	@MinIncrementFrameSize.setter
	def MinIncrementFrameSize(self, value):
		self._set_attribute('minIncrementFrameSize', value)

	@property
	def MinKbpsRate(self):
		"""The rate at which minimum frames are sent per kbps.

		Returns:
			number
		"""
		return self._get_attribute('minKbpsRate')
	@MinKbpsRate.setter
	def MinKbpsRate(self, value):
		self._set_attribute('minKbpsRate', value)

	@property
	def MinQuickSearchLoadRate(self):
		"""Sets the minum Quick Search load rate

		Returns:
			number
		"""
		return self._get_attribute('minQuickSearchLoadRate')
	@MinQuickSearchLoadRate.setter
	def MinQuickSearchLoadRate(self, value):
		self._set_attribute('minQuickSearchLoadRate', value)

	@property
	def MinRandomFrameSize(self):
		"""The minimum random frame size to be sent.

		Returns:
			number
		"""
		return self._get_attribute('minRandomFrameSize')
	@MinRandomFrameSize.setter
	def MinRandomFrameSize(self, value):
		self._set_attribute('minRandomFrameSize', value)

	@property
	def Numtrials(self):
		"""Defines how many times each frame size will be tested.

		Returns:
			number
		"""
		return self._get_attribute('numtrials')
	@Numtrials.setter
	def Numtrials(self, value):
		self._set_attribute('numtrials', value)

	@property
	def PercentMaxRate(self):
		"""The percentage of the maximum rate that is specified.

		Returns:
			number
		"""
		return self._get_attribute('percentMaxRate')
	@PercentMaxRate.setter
	def PercentMaxRate(self, value):
		self._set_attribute('percentMaxRate', value)

	@property
	def PortDelayEnabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('portDelayEnabled')
	@PortDelayEnabled.setter
	def PortDelayEnabled(self, value):
		self._set_attribute('portDelayEnabled', value)

	@property
	def PortDelayUnit(self):
		"""Sets the port delay unit in which it will be measured

		Returns:
			str(bytes|nanoseconds)
		"""
		return self._get_attribute('portDelayUnit')
	@PortDelayUnit.setter
	def PortDelayUnit(self, value):
		self._set_attribute('portDelayUnit', value)

	@property
	def PortDelayValue(self):
		"""Sets the port delay value

		Returns:
			number
		"""
		return self._get_attribute('portDelayValue')
	@PortDelayValue.setter
	def PortDelayValue(self, value):
		self._set_attribute('portDelayValue', value)

	@property
	def ProtocolItem(self):
		"""Protocol Items

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/vport|/api/v1/sessions/1/ixnetwork/vport?deepchild=lan])
		"""
		return self._get_attribute('protocolItem')
	@ProtocolItem.setter
	def ProtocolItem(self, value):
		self._set_attribute('protocolItem', value)

	@property
	def QuickSearchFrameLossUnit(self):
		"""Sets the quick search frame loss unit

		Returns:
			str(%)
		"""
		return self._get_attribute('quickSearchFrameLossUnit')
	@QuickSearchFrameLossUnit.setter
	def QuickSearchFrameLossUnit(self, value):
		self._set_attribute('quickSearchFrameLossUnit', value)

	@property
	def QuickSearchLoadUnit(self):
		"""Sets the quick search load unit

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('quickSearchLoadUnit')
	@QuickSearchLoadUnit.setter
	def QuickSearchLoadUnit(self, value):
		self._set_attribute('quickSearchLoadUnit', value)

	@property
	def QuickSearchResolution(self):
		"""Sets the quick search resolution

		Returns:
			number
		"""
		return self._get_attribute('quickSearchResolution')
	@QuickSearchResolution.setter
	def QuickSearchResolution(self, value):
		self._set_attribute('quickSearchResolution', value)

	@property
	def QuickSearchSearchType(self):
		"""Sets the quick search type

		Returns:
			str(linear|perFlow|perPort|perTrafficItem)
		"""
		return self._get_attribute('quickSearchSearchType')
	@QuickSearchSearchType.setter
	def QuickSearchSearchType(self, value):
		self._set_attribute('quickSearchSearchType', value)

	@property
	def QuickSearchTolerance(self):
		"""Sets the quick search tolerance

		Returns:
			number
		"""
		return self._get_attribute('quickSearchTolerance')
	@QuickSearchTolerance.setter
	def QuickSearchTolerance(self, value):
		self._set_attribute('quickSearchTolerance', value)

	@property
	def RateSelect(self):
		"""It selects the rate value of the protocol.

		Returns:
			str(fpsRate|kbpsRate|percentMaxRate)
		"""
		return self._get_attribute('rateSelect')
	@RateSelect.setter
	def RateSelect(self, value):
		self._set_attribute('rateSelect', value)

	@property
	def ReportSequenceError(self):
		"""Reports sequence errors in the test result.

		Returns:
			bool
		"""
		return self._get_attribute('reportSequenceError')
	@ReportSequenceError.setter
	def ReportSequenceError(self, value):
		self._set_attribute('reportSequenceError', value)

	@property
	def ReportTputRateUnit(self):
		"""The report throughput rate.

		Returns:
			str(gbps|gBps|kbps|kBps|mbps|mBps)
		"""
		return self._get_attribute('reportTputRateUnit')
	@ReportTputRateUnit.setter
	def ReportTputRateUnit(self, value):
		self._set_attribute('reportTputRateUnit', value)

	@property
	def Resolution(self):
		"""Specifies the resolution of the iteration. The difference between the real rate transmission in two consecutive iterations, expressed as a percentage, is compared with the resolution value. When the difference is smaller than the value specified for the resolution, the test stops.

		Returns:
			number
		"""
		return self._get_attribute('resolution')
	@Resolution.setter
	def Resolution(self, value):
		self._set_attribute('resolution', value)

	@property
	def Rfc2889ordering(self):
		"""Enables ordering.

		Returns:
			str(noOrdering|unchanged|val2889Ordering)
		"""
		return self._get_attribute('rfc2889ordering')
	@Rfc2889ordering.setter
	def Rfc2889ordering(self, value):
		self._set_attribute('rfc2889ordering', value)

	@property
	def SendFullyMeshed(self):
		"""Indicates the source group mapping type used for sending data.

		Returns:
			bool
		"""
		return self._get_attribute('sendFullyMeshed')
	@SendFullyMeshed.setter
	def SendFullyMeshed(self, value):
		self._set_attribute('sendFullyMeshed', value)

	@property
	def ShowDetailedBinaryResults(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('showDetailedBinaryResults')
	@ShowDetailedBinaryResults.setter
	def ShowDetailedBinaryResults(self, value):
		self._set_attribute('showDetailedBinaryResults', value)

	@property
	def StepComboLoadRate(self):
		"""The step rate of the binary algorithm for Combo Load Type.

		Returns:
			number
		"""
		return self._get_attribute('stepComboLoadRate')
	@StepComboLoadRate.setter
	def StepComboLoadRate(self, value):
		self._set_attribute('stepComboLoadRate', value)

	@property
	def StepFrameLossUnit(self):
		"""The step frame loss unit.

		Returns:
			str(%|frames)
		"""
		return self._get_attribute('stepFrameLossUnit')
	@StepFrameLossUnit.setter
	def StepFrameLossUnit(self, value):
		self._set_attribute('stepFrameLossUnit', value)

	@property
	def StepIncrementFrameSize(self):
		"""The incremental step value of the frame size.

		Returns:
			number
		"""
		return self._get_attribute('stepIncrementFrameSize')
	@StepIncrementFrameSize.setter
	def StepIncrementFrameSize(self, value):
		self._set_attribute('stepIncrementFrameSize', value)

	@property
	def StepLoadUnit(self):
		"""The step load unit.

		Returns:
			str(bpsRate|fpsRate|gbpsRate|gBpsRate|kbpsRate|kBpsRate|mbpsRate|mBpsRate|percentMaxRate)
		"""
		return self._get_attribute('stepLoadUnit')
	@StepLoadUnit.setter
	def StepLoadUnit(self, value):
		self._set_attribute('stepLoadUnit', value)

	@property
	def StepStepLoadRate(self):
		"""The step rate of the binary algorithm.

		Returns:
			number
		"""
		return self._get_attribute('stepStepLoadRate')
	@StepStepLoadRate.setter
	def StepStepLoadRate(self, value):
		self._set_attribute('stepStepLoadRate', value)

	@property
	def StepTolerance(self):
		"""The value of the tolerance level for Step Load Type.

		Returns:
			number
		"""
		return self._get_attribute('stepTolerance')
	@StepTolerance.setter
	def StepTolerance(self, value):
		self._set_attribute('stepTolerance', value)

	@property
	def SupportedTrafficTypes(self):
		"""The traffic types supported.

		Returns:
			str
		"""
		return self._get_attribute('supportedTrafficTypes')
	@SupportedTrafficTypes.setter
	def SupportedTrafficTypes(self, value):
		self._set_attribute('supportedTrafficTypes', value)

	@property
	def Tolerance(self):
		"""The level of acceptable threshold.

		Returns:
			number
		"""
		return self._get_attribute('tolerance')
	@Tolerance.setter
	def Tolerance(self, value):
		self._set_attribute('tolerance', value)

	@property
	def TrafficType(self):
		"""It signifies the traffic type.

		Returns:
			str(burstyLoading|constantLoading)
		"""
		return self._get_attribute('trafficType')
	@TrafficType.setter
	def TrafficType(self, value):
		self._set_attribute('trafficType', value)

	@property
	def TxDelay(self):
		"""Specifies the amount of delay after every transmit.

		Returns:
			number
		"""
		return self._get_attribute('txDelay')
	@TxDelay.setter
	def TxDelay(self, value):
		self._set_attribute('txDelay', value)

	@property
	def UsePercentOffsets(self):
		"""Uses percentage offset value.

		Returns:
			bool
		"""
		return self._get_attribute('usePercentOffsets')
	@UsePercentOffsets.setter
	def UsePercentOffsets(self, value):
		self._set_attribute('usePercentOffsets', value)

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
