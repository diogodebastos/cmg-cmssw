# This file is the authoritative source of the order of tracking
# iterations. It is used in RECO, DQM, and VALIDATION. Note that here
# InitialStepPreSplitting is not counted as an iteration.
import FWCore.ParameterSet.Config as cms

_defaultEra = ""
_nonDefaultEras = ["trackingLowPU", "trackingPhase1", "trackingPhase1PU70", "trackingPhase2PU140"]
_allEras = [_defaultEra] + _nonDefaultEras

_iterations = [
    "InitialStep",
    "DetachedTripletStep",
    "LowPtTripletStep",
    "PixelPairStep",
    "MixedTripletStep",
    "PixelLessStep",
    "TobTecStep",
    "JetCoreRegionalStep",
]
_iterations_trackingLowPU = [
    "InitialStep",
    "LowPtTripletStep",
    "PixelPairStep",
    "DetachedTripletStep",
    "MixedTripletStep",
    "PixelLessStep",
    "TobTecStep",
]
_iterations_trackingPhase1 = [
    "InitialStep",
    "LowPtQuadStep",
    "HighPtTripletStep",
    "LowPtTripletStep",
    "DetachedQuadStep",
    "DetachedTripletStep",
    "MixedTripletStep",
    "PixelLessStep",
    "TobTecStep",
    "JetCoreRegionalStep",
]
_iterations_trackingPhase1PU70 = [
    "InitialStep",
    "HighPtTripletStep",
    "LowPtQuadStep",
    "LowPtTripletStep",
    "DetachedQuadStep",
    "MixedTripletStep",
    "PixelPairStep",
    "TobTecStep",
]
_iterations_trackingPhase2PU140 = [
    "InitialStep",
    "HighPtTripletStep",
    "LowPtQuadStep",
    "LowPtTripletStep",
    "DetachedQuadStep",
    "PixelPairStep",
]
_iterations_muonSeeded = [
    "MuonSeededStepInOut",
    "MuonSeededStepOutIn",
]
#Phase2 : just muon Seed InOut is used in this moment
_iterations_muonSeeded_trackingPhase2PU140 = [
    "MuonSeededStepInOut",
]
_multipleSeedProducers = {
    "MixedTripletStep": ["A", "B"],
    "TobTecStep": ["Pair", "Tripl"],
}
_multipleSeedProducers_trackingLowPU = {
    "MixedTripletStep": ["A", "B"],
}
_multipleSeedProducers_trackingPhase1 = _multipleSeedProducers
_multipleSeedProducers_trackingPhase1PU70 = _multipleSeedProducers_trackingLowPU
_multipleSeedProducers_trackingPhase2PU140 = {}
_oldStyleHasSelector = set([
    "InitialStep",
    "HighPtTripletStep",
    "LowPtQuadStep",
    "LowPtTripletStep",
    "PixelPairStep",
    "PixelLessStep",
    "TobTecStep",
])

from RecoLocalTracker.SubCollectionProducers.trackClusterRemover_cfi import trackClusterRemover as _trackClusterRemover
_trackClusterRemoverBase = _trackClusterRemover.clone(
    maxChi2                                  = 9.0,
    pixelClusters                            = "siPixelClusters",
    stripClusters                            = "siStripClusters",
    TrackQuality                             = 'highPurity',
    minNumberOfLayersWithMeasBeforeFiltering = 0,
)

#Phase2 : configuring the phase2 track Cluster Remover
from RecoLocalTracker.SubCollectionProducers.phase2trackClusterRemover_cfi import *
__trackClusterRemoverBase_Phase2PU140 = phase2trackClusterRemover.clone(
    maxChi2                                  = cms.double(9.0),
    phase2pixelClusters                      = cms.InputTag("siPixelClusters"),
    phase2OTClusters                         = cms.InputTag("siPhase2Clusters"),
    TrackQuality                             = cms.string('highPurity'),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
)

def postfix(era):
    return "_"+era if era != _defaultEra else era

def _modulePrefix(iteration):
    return iteration[0].lower()+iteration[1:]

def _clusterRemover(iteration):
    return _modulePrefix(iteration)+"Clusters"

def _tracks(iteration):
    return _modulePrefix(iteration)+"Tracks"

def _classifier(iteration, oldStyle=False, oldStyleQualityMasks=False):
    pre = _modulePrefix(iteration)
    if oldStyle:
        if iteration in _oldStyleHasSelector:
            return pre+"Selector:" + ("QualityMasks" if oldStyleQualityMasks else pre)
        else:
            return pre
    else:
        return pre+":QualityMasks"

def allEras():
    return _allEras

def nonDefaultEras():
    return _nonDefaultEras

def createEarlySequence(era, modDict):
    pf = postfix(era)
    seq = cms.Sequence()
    for it in globals()["_iterations"+pf]:
        seq += modDict[it]
    return seq

def iterationAlgos(era):
  if era == "trackingPhase2PU140": return [_modulePrefix(i) for i in globals()["_iterations"+postfix(era)] + _iterations_muonSeeded_trackingPhase2PU140]
  return [_modulePrefix(i) for i in globals()["_iterations"+postfix(era)] + _iterations_muonSeeded]

def _seedOrTrackProducers(era, typ):
    ret = []
    pf = postfix(era)
    iters = globals()["_iterations"+pf]
    if typ == "Seeds":
        multipleSeedProducers = globals()["_multipleSeedProducers"+pf]
    else:
        multipleSeedProducers = None
    for i in iters:
        seeder = _modulePrefix(i)+typ
        if multipleSeedProducers is not None and i in multipleSeedProducers:
            ret.extend([seeder+m for m in multipleSeedProducers[i]])
        else:
            ret.append(seeder)

    if era == "trackingPhase2PU140":
        for i in _iterations_muonSeeded_trackingPhase2PU140:
            ret.append(_modulePrefix(i).replace("Step", typ))
    else :
        for i in _iterations_muonSeeded:
            ret.append(_modulePrefix(i).replace("Step", typ))

    return ret

def seedProducers(era):
    return _seedOrTrackProducers(era, "Seeds")

def trackProducers(era):
    return _seedOrTrackProducers(era, "Tracks")

def clusterRemoverForIter(iteration, era="", module=None):
    if module is None:
        module = _trackClusterRemoverBase.clone()
    if era == "trackingPhase2PU140":
        module = __trackClusterRemoverBase_Phase2PU140.clone()

    pf = postfix(era)
    iters = globals()["_iterations"+pf]
    try:
        ind = iters.index(iteration)
    except ValueError:
        # if the iteration is not active in era, just return the same
        return module

    if ind == 0:
        raise Exception("Iteration %s is the first iteration in era %s, asking cluster remover configuration does not make sense" % (iteration, era))
    prevIter = iters[ind-1]

    customize = dict(
        trajectories          = _tracks(prevIter),
        oldClusterRemovalInfo = _clusterRemover(prevIter) if ind >= 2 else "", # 1st iteration does not have cluster remover
    )
    if era == "trackingPhase1PU70" or era == "trackingPhase2PU140":
        customize["overrideTrkQuals"] = _classifier(prevIter, oldStyle=True) # old-style selector
    elif era == "trackingLowPU":
        customize["overrideTrkQuals"] = _classifier(prevIter, oldStyle=True, oldStyleQualityMasks=True) # old-style selector with 'QualityMasks' instance label
    else:
        customize["trackClassifier"] = _classifier(prevIter)
#    overrideTrkQuals                         = cms.InputTag('initialStepSelector','initialStep'),

    return module.clone(**customize)
