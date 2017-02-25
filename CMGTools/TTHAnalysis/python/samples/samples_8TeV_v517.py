from CMGTools.TTHAnalysis.samples.getFiles import getFiles
import CMGTools.RootTools.fwlite.Config as cfg
import os

patOld='PAT_CMG_V5_16_0'
pat='PAT_CMG_V5_17_0'
patNew='PAT_CMG_V5_18_0'
patPF='CMGPF_V5_16_0'
filepattern = 'cmgTuple.*root'
userName='cmgtools'



################## Triggers


triggers_mumu = ["HLT_Mu17_Mu8_v*","HLT_Mu17_TkMu8_v*"]
triggers_ee   = ["HLT_Ele17_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_v*",
                 "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",
                 "HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v*"]

triggers_mue   = [
    "HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",
    "HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*"
    ]

triggersMC_mumu = ["HLT_Mu17_Mu8_v*","HLT_Mu17_TkMu8_v*"]

triggersMC_ee   = ["HLT_Ele17_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_v*",
                   "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",
                   "HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v*"]

triggersMC_mue   = ["HLT_Ele17_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_Ele8_CaloIdT_TrkIdVL_CaloIsoVL_TrkIsoVL_v*",
                    "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",
                    "HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v*",
                    "HLT_Mu17_Mu8_v*",
                    "HLT_Mu17_TkMu8_v*",
                    "HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",
                    "HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*",
                    "HLT_IsoMu24_eta2p1_v*",
                    "HLT_Ele27_WP80_v*"
                   ]

triggers_1mu = [ 'HLT_IsoMu24_eta2p1_v*' ]
triggersMC_1mu  = triggers_1mu;

triggers_1e = [ "HLT_Ele27_WP80_v*" ]
triggersMC_1e = triggers_1e; # check this !!!

triggersFR_1mu  = [ 'HLT_Mu5_v*', 'HLT_RelIso1p0Mu5_v*', 'HLT_Mu12_v*', 'HLT_Mu24_eta2p1_v*', 'HLT_Mu40_eta2p1_v*' ]
triggersFR_mumu = [ 'HLT_Mu17_Mu8_v*', 'HLT_Mu17_TkMu8_v*', 'HLT_Mu8_v*', 'HLT_Mu17_v*' ]
triggersFR_1e   = [ 'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*', 'HLT_Ele17_CaloIdL_CaloIsoVL_v*', 'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v*', 'HLT_Ele8__CaloIdL_CaloIsoVL_v*']
triggersFR_mue  = triggers_mue[:]
triggersFR_MC = triggersFR_1mu + triggersFR_mumu + triggersFR_1e + triggersFR_mue


### ----> for the SUS-13-007

triggers_1muHT = ["HLT_PFHT350_Mu15_PFMET45_v*","HLT_PFHT350_Mu15_PFMET50_v*",
                  "HLT_PFNoPUHT350_Mu15_PFMET_45_v*","HLT_PFHT350_Mu15_PFMET50_v*",
                  "HLT_PFHT400_Mu5_PFMET45_v*","HLT_PFHT400_Mu5_PFMET50_v*",
                  "HLT_PFNoPUHT400_Mu5_PFMET45_v*","HLT_PFNoPUHT400_Mu5_PFMET50_v*",
                  "HLT_Mu40_PFHT350_v*","HLT_Mu60_PFHT350_v*",
                  "HLT_Mu40_PFNoPUHT350_v*","HLT_Mu60_PFNoPUHT350_v*"
                  ]

triggers_1eleHT = ["HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*","HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",
                   "HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*","HLT_CleanPFNoPUHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v*",
                   "HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*","HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET60_v*",
                   "HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v*","HLT_CleanPFNoPUHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET60_v*",
                   "HLT_CleanPFHT300_Ele40_CaloIdVT_CaloIsoVL_TrkIdT_v*","HLT_CleanPFHT300_Ele60_CaloIdVT_CaloIsoVL_TrkIdT_v*",                   
                   "HLT_CleanPFNoPUHT300_Ele40_CaloIdVT_CaloIsoVL_TrkIdT_ v*","HLT_CleanPFNoPUHT300_Ele60_CaloIdVT_CaloIsoVL_TrkIdT_ v*"
                   ]


### ----> for the SUS-13-019

triggers_HT650 = ["HLT_PFHT650_v*","HLT_PFNoPUHT650_v*"]
triggers_MET150 = ["HLT_PFMET150_v*"]
triggers_HTMET = ["HLT_PFHT350_PFMET100_v*","HLT_PFNoPUHT350_PFMET100_v*"]

#####COMPONENT CREATOR

from CMGTools.TTHAnalysis.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

#-----------MC---------------
## --- TTH ---
TTH      =kreator.makeMCComponent('TTH','/TTH_Inclusive_M-125_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+pat,userName,filepattern)
TTH122   =kreator.makeMCComponent('TTH122','/TTH_Inclusive_M-122_5_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
TTH127   =kreator.makeMCComponent('TTH127','/TTH_Inclusive_M-127_5_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)

## --- TTH + V ---
TTWJets  =kreator.makeMCComponent('TTWJets','/TTWJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+pat,userName,filepattern)
TTZJets  =kreator.makeMCComponent('TTZJets','/TTZJets_8TeV-madgraph_v2/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+pat,userName,filepattern)
TTWWJets =kreator.makeMCComponent('TTWWJets','/TTWWJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)
## --- same as above but aMC@NLO ---
TTWnlo   =kreator.makeMCComponent('TTWnlo','/TTbarW_8TeV-aMCatNLO-herwig/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/V5_B/'+patPF,userName,filepattern)
TTZnlo   =kreator.makeMCComponent('TTZnlo','/ttbarZ_8TeV-Madspin_aMCatNLO-herwig/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/V5_B/'+patPF,userName,filepattern)

## --- TTH + gamma ---
TTG =kreator.makeMCComponent('TTG','/TTGJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/V5_B/'+patPF,userName,filepattern)

## ---- DIBOSON, PYTHIA INCLUSIVE ----
WW = kreator.makeMCComponent('WW', '/WW_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)
WZ = kreator.makeMCComponent('WZ', '/WZ_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)
ZZ = kreator.makeMCComponent('ZZ', '/ZZ_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)
## ---- DIBOSON, MADGRAPH EXCLUSIVE ----
WWJets   =kreator.makeMCComponent('WWJets','/WWJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
WZJets   =kreator.makeMCComponent('WZJets','/WZJetsTo3LNu_TuneZ2_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)     
ZZJets4L =kreator.makeMCComponent('ZZJets4L','/ZZJetsTo4L_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern) 
## ---- DIBOSONS, POWHEG ----
ZZ2e2mu  =kreator.makeMCComponent('ZZ2e2mu','/ZZTo2e2mu_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+patNew,userName,filepattern)
ZZ2e2tau =kreator.makeMCComponent('ZZ2e2tau','/ZZTo2e2tau_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+patNew,userName,filepattern)
ZZ2mu2tau=kreator.makeMCComponent('ZZ2mu2tau','/ZZTo2mu2tau_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+patNew,userName,filepattern)
ZZTo4mu  =kreator.makeMCComponent('ZZTo4mu','/ZZTo4mu_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+patNew,userName,filepattern)
ZZTo4tau =kreator.makeMCComponent('ZZTo4tau','/ZZTo4tau_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+patNew,userName,filepattern)
ZZTo4e   =kreator.makeMCComponent('ZZTo4e','/ZZTo4e_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+patNew,userName,filepattern)

## --- MULTIBOSON -----
WWWJets  =kreator.makeMCComponent('WWWJets','/WWWJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)
WWZJets  =kreator.makeMCComponent('WWZJets','/WWZNoGstarJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)
WZZJets  =kreator.makeMCComponent('WZZJets','/WZZNoGstarJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)
ZZZJets  =kreator.makeMCComponent('ZZZJets','/ZZZNoGstarJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)

## --- BOSON + PHOTON
#ZG =kreator.makeMCComponent('ZG','/ZGToLLG_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)
#WGToLNuG =kreator.makeMCComponent('WGToLNuG','/WGToLNuG_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)
## --- MULTIBOSON + PHOTON
WWGJets  =kreator.makeMCComponent('WWGJets','/WWGJets_8TeV-madgraph_v2/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)


## ---- TTBAR -----
TTLep    =kreator.makeMCComponent('TTLep','/TTTo2L2Nu2B_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
TTJets   =kreator.makeMCComponent('TTJets','/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)
TTJetsLep=kreator.makeMCComponent('TTJetsLep','/TTJets_FullLeptMGDecays_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/V5_B/'+patNew,userName,filepattern)
TTJetsSem=kreator.makeMCComponent('TTJetsSem','/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V19_ext1-v1/AODSIM/V5/'+patNew,userName,filepattern)
TTJetsSem2=kreator.makeMCComponent('TTJetsSem2','/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V19_ext2-v1/AODSIM/V5/'+patNew,userName,filepattern)
TTJetsHad=kreator.makeMCComponent('TTJetsHad','/TTJets_HadronicMGDecays_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A_ext-v1/AODSIM/V5/'+patNew,userName,filepattern)

# ---- SINGLE TOP ----
TtW       =kreator.makeMCComponent('TtW','/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)
TbartW    =kreator.makeMCComponent('TbartW','/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)
Ttch      =kreator.makeMCComponent('Ttch','/T_t-channel_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)
Tbartch   =kreator.makeMCComponent('Tbartch','/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)
Tsch      =kreator.makeMCComponent('Tsch','/T_s-channel_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)
Tbarsch   =kreator.makeMCComponent('Tbarsch','/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)

# ---- Z + JETS
DYJetsM10=kreator.makeMCComponent('DYJetsM10','/DYJetsToLL_M-10To50filter_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
DYJetsM50=kreator.makeMCComponent('DYJetsM50','/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)
DY1JetsM50=kreator.makeMCComponent('DY1JetsM50','/DY1JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
DY2JetsM50=kreator.makeMCComponent('DY2JetsM50','/DY2JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
DY3JetsM50=kreator.makeMCComponent('DY3JetsM50','/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
DY4JetsM50=kreator.makeMCComponent('DY4JetsM50','/DY4JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)


# ---- W + JETS
WJets    =kreator.makeMCComponent('WJets','/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/V5_B/'+patPF,userName,filepattern)
W1Jets   =kreator.makeMCComponent('W1Jets','/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
W2Jets   =kreator.makeMCComponent('W2Jets','/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
W3Jets   =kreator.makeMCComponent('W3Jets','/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
W4Jets   =kreator.makeMCComponent('W4Jets','/W4JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
WJets_HT250To300=kreator.makeMCComponent('WJets_HT250To300','/WJetsToLNu_HT-250To300_8TeV-madgraph_v2/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)
WJets_HT300To400=kreator.makeMCComponent('WJets_HT300To400','/WJetsToLNu_HT-300To400_8TeV-madgraph_v2/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)
WJets_HT400ToInf=kreator.makeMCComponent('WJets_HT400ToInf','/WJetsToLNu_HT-400Toinf_8TeV-madgraph_v2/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+patPF,userName,filepattern)
WJetsPtW50To70 =kreator.makeMCComponent('WJets_PtW-50To70','/WJetsToLNu_PtW-50To70_TuneZ2star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)
WJetsPtW70To100=kreator.makeMCComponent('WJets_PtW-70To100','/WJetsToLNu_PtW-70To100_TuneZ2star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)
WJetsPtW100    =kreator.makeMCComponent('WJets_PtW-100','/WJetsToLNu_PtW-100_TuneZ2star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)

# ---- Z inv + JETS
ZNuNu50HT100=kreator.makeMCComponent('ZJetsToNuNu50HT100','/ZJetsToNuNu_50_HT_100_TuneZ2Star_8TeV_madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+patNew,userName,filepattern)
ZNuNu100HT200=kreator.makeMCComponent('ZJetsToNuNu100HT200','/ZJetsToNuNu_100_HT_200_TuneZ2Star_8TeV_madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+patNew,userName,filepattern)
ZNuNu200HT400=kreator.makeMCComponent('ZJetsToNuNu200HT400','/ZJetsToNuNu_200_HT_400_TuneZ2Star_8TeV_madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+patNew,userName,filepattern)
ZNuNu400=kreator.makeMCComponent('ZJetsToJetsToNuNu400','/ZJetsToNuNu_400_HT_inf_TuneZ2Star_8TeV_madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+patNew,userName,filepattern)

# ---- QCD
QCDMuPt15=kreator.makeMCComponent('QCDMuPt15','/QCD_Pt_20_MuEnrichedPt_15_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v3/AODSIM/V5/'+patNew,userName,filepattern)
#QCDElPt30To80=kreator.makeMCComponent('QCDElPt30To80','//QCD_Pt_30_80_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)
#QCDElPt80To170=kreator.makeMCComponent('QCDElPt80To170','//QCD_Pt_80_170_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/'+pat,userName,filepattern)

# ------ RARE PROCESSES -----
TBZToLL =kreator.makeMCComponent('TBZToLL', '/TBZToLL_4F_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/V5/'+patNew,userName,filepattern)
WmWmqq  =kreator.makeMCComponent('WmWmqq',  '/WmWmqq_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+patNew,userName,filepattern)
WpWpqq  =kreator.makeMCComponent('WpWpqq',  '/WpWpqq_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5/'+patNew,userName,filepattern)

# ------ MORE SAMPLES FROM SEZEN (patPF) ----
#/Jet/Run2012A-22Jan2013-v1/AOD/CMGPF_V5_16_0
#/HT/Run2012A-22Jan2013-v1/AOD/CMGPF_V5_16_0
#/JetHT/Run2012B-22Jan2013-v1/AOD/CMGPF_V5_16_0
#/JetHT/Run2012C-22Jan2013-v1/AOD/CMGPF_V5_16_0
#/JetHT/Run2012D-22Jan2013-v1/AOD/CMGPF_V5_16_0
#/QCD_HT-100To250_TuneZ2star_8TeV-madgraph-pythia/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/CMGPF_V5_16_0
#/QCD_HT-250To500_TuneZ2star_8TeV-madgraph-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/CMGPF_V5_16_0
#/QCD_HT-500To1000_TuneZ2star_8TeV-madgraph-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/CMGPF_V5_16_0
#/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/CMGPF_V5_16_0
# ----- MORE FRMO MARKUS -------------
# /DYJetsToLL_PtZ-50To70_TuneZ2star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_17_0
# /DYJetsToLL_PtZ-70To100_TuneZ2star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/V5_B/PAT_CMG_V5_17_0
# /DYJetsToLL_PtZ-100_TuneZ2star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/V5_B/PAT_CMG_V5_17_0
# /WJetsToLNu_PtW-100_TuneZ2star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_17_0
# /WJetsToLNu_PtW-70To100_TuneZ2star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_17_0
# /WJetsToLNu_PtW-50To70_TuneZ2star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_17_0
# /DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_17_0_2nd
# /DYToTauTau_M-20_CT10_TuneZ2star_v2_8TeV-powheg-tauola-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/V5_B/PAT_CMG_V5_17_0_2nd

# ----- FINAL LISTS OF BACKGROUNDS ------
#   ## Critical samples (major signals and backgrounds, and a few small samples)
mcSamples_1 = [ TTH,TTWJets,TTZJets,TTWWJets,WWWJets,WWZJets,TTG,DYJetsM50,TTJetsLep,TTJetsSem,TTJets,TtW,TbartW,WZJets,ZZJets4L,WWJets,DYJetsM10, ZZ2e2mu,ZZ2e2tau,ZZ2mu2tau,ZZTo4mu,ZZTo4e,ZZTo4tau,
                W1Jets,W2Jets,W3Jets,W4Jets,WJets_HT250To300,WJets_HT300To400,WJets_HT400ToInf,DY1JetsM50,DY2JetsM50,DY3JetsM50,DY4JetsM50,TTJetsSem,ZNuNu50HT100,ZNuNu100HT200,ZNuNu200HT400,ZNuNu400 ]
#   ## Minor samples and backgrounds 
mcSamples_2 = [ Tsch,Tbarsch,Ttch,Tbartch,WZZJets,ZZZJets,WWGJets,TTLep,TTJetsSem2,TTJetsHad, TBZToLL,WmWmqq,WpWpqq,TTH122,TTH127,WJetsPtW50To70,WJetsPtW70To100,WJetsPtW100]
#   mcSamples_2 = [ TTH122,TTH127,DYJetsM10,TTLep,WWJets,TTJets,Tsch,Tbarsch,Ttch,Tbartch,W1Jets,W2Jets,W3Jets,W4Jets,TTJetsHad,DY1JetsM50, ]
#   ## Cross-check samples, ... 
mcSamples_3 = [ TTWnlo,TTZnlo,WJets,QCDMuPt15 ]
#   ## Samples we don't use
mcSamples_4 = [ WW,WZ,ZZ ]


# ------- SUSY SIGNAL SAMPLES ------
T1tttt_2J_1 = kreator.makeMCComponent('T1tttt_2J_1', '/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-400to750_mLSP-1_50GeVX50GeV_Binning/Summer12-START52_V9_FSIM-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
T1tttt_2J_2 = kreator.makeMCComponent('T1tttt_2J_2', '/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-800to1400_mLSP-1_50GeVX50GeV_Binning/Summer12-START52_V9_FSIM-v2/AODSIM/V5_B/'+patNew,userName,filepattern)
T1tttt_2J_3 = kreator.makeMCComponent('T1tttt_2J_3', '/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-400to750_mLSP-25to550_50GeVX50GeV_Binning/Summer12-START52_V9_FSIM-v1/AODSIM/V5_B/'+patNew,userName,filepattern)
T1tttt_2J_4 = kreator.makeMCComponent('T1tttt_2J_4', '/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-775to1075_mLSP-25to500_50GeVX50GeV_Binning/Summer12-START52_V9_FSIM-v3/AODSIM/V5_B/'+patNew,userName,filepattern)
T1tttt_2J_5 = kreator.makeMCComponent('T1tttt_2J_5', '/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-775to1075_mLSP-525to875_50GeVX50GeV_Binning/Summer12-START52_V9_FSIM-v3/AODSIM/V5_B/'+patNew,userName,filepattern)
T1tttt_2J_6 = kreator.makeMCComponent('T1tttt_2J_6', '/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/Summer12-START52_V9_FSIM-v2/AODSIM/V5_B/'+patNew,userName,filepattern)
T1tttt_2J_7 = kreator.makeMCComponent('T1tttt_2J_7', '/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-525to1000_25GeVX25GeV_Binning/Summer12-START52_V9_FSIM-v2/AODSIM/V5_B/'+patNew,userName,filepattern)
T1tttt_2J_8 = kreator.makeMCComponent('T1tttt_2J_8', '/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-1025to1200_50GeVX50GeV_Binning/Summer12-START52_V9_FSIM-v1/AODSIM/V5_B/'+patNew,userName,filepattern)

T5VV_2J_1 = kreator.makeMCComponent('T5VV_2J_1', '/SMS-T5VV_2J_mGo-400to750_mLSP-25to525_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T5VV_2J_2 = kreator.makeMCComponent('T5VV_2J_2', '/SMS-T5VV_2J_mGo-800to1100_mLSP-25to525_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T5VV_2J_3 = kreator.makeMCComponent('T5VV_2J_3', '/SMS-T5VV_2J_mGo-800to1100_mLSP-575to875_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T5VV_2J_4 = kreator.makeMCComponent('T5VV_2J_4', '/SMS-T5VV_2J_mGo-1150to1400_mLSP-25to525_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T5VV_2J_5 = kreator.makeMCComponent('T5VV_2J_5', '/SMS-T5VV_2J_mGo-1150to1400_mLSP-550to700_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T5VV_2J_6 = kreator.makeMCComponent('T5VV_2J_6', '/SMS-T5VV_2J_mGo-1150to1400_mLSP-725to850_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T5VV_2J_7 = kreator.makeMCComponent('T5VV_2J_7', '/SMS-T5VV_2J_mGo-1150to1400_mLSP-875to1175_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)

T2DegenerateStop_2J_1 = kreator.makeMCComponent('T2DegenerateStop_2J_1', '/SMS-T2DegenerateStop_2J_mStop-100to150_mLSP-20to140_TuneZ2star_8TeV-madgraph-tauolapp/Summer12-START53_V19_FSIM_PU_S12-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2DegenerateStop_2J_2 = kreator.makeMCComponent('T2DegenerateStop_2J_2', '/SMS-T2DegenerateStop_2J_mStop-175to225_mLSP-95to215_TuneZ2star_8TeV-madgraph-tauolapp/Summer12-START53_V19_FSIM_PU_S12-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2DegenerateStop_2J_3 = kreator.makeMCComponent('T2DegenerateStop_2J_3', '/SMS-T2DegenerateStop_2J_mStop-250to300_mLSP-170to290_TuneZ2star_8TeV-madgraph-tauolapp/Summer12-START53_V19_FSIM_PU_S12-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2DegenerateStop_2J_4 = kreator.makeMCComponent('T2DegenerateStop_2J_4', '/SMS-T2DegenerateStop_2J_mStop-325to375_mLSP-245to365_TuneZ2star_8TeV-madgraph-tauolapp/Summer12-START53_V19_FSIM_PU_S12-v1/AODSIM/V5/'+patNew,userName,filepattern)

T2qq_2J_1 = kreator.makeMCComponent('T2qq_2J_1', '/SMS-T2qq_2J_mSquark-300to450_mLSP-1to400_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2qq_2J_2 = kreator.makeMCComponent('T2qq_2J_2', '/SMS-T2qq_2J_mSquark-500to750_mLSP-1to700_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2qq_2J_3 = kreator.makeMCComponent('T2qq_2J_3', '/SMS-T2qq_2J_mSquark-800to1000_mLSP-1to950_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2qq_2J_4 = kreator.makeMCComponent('T2qq_2J_4', '/SMS-T2qq_2J_mSquark-1050to1200_mLSP-1to1150_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)

T2bb_2J_1 = kreator.makeMCComponent('T2bb_2J_1', '/SMS-T2bb_2J_mSbottom-100to475_mLSP-1to465_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2bb_2J_2 = kreator.makeMCComponent('T2bb_2J_2', '/SMS-T2bb_2J_mSbottom-500to800_mLSP-1to790_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)

T2tt_2J_1 = kreator.makeMCComponent('T2tt_2J_1', '/SMS-T2tt_mStop-150to350_mLSP-0to250_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2tt_2J_2 = kreator.makeMCComponent('T2tt_2J_2', '/SMS-T2tt_mStop-375to475_mLSP-0to375_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2tt_2J_3 = kreator.makeMCComponent('T2tt_2J_3', '/SMS-T2tt_mStop-500to650_mLSP-0to225_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2tt_2J_4 = kreator.makeMCComponent('T2tt_2J_4', '/SMS-T2tt_mStop-500to650_mLSP-250to550_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2tt_2J_5 = kreator.makeMCComponent('T2tt_2J_5', '/SMS-T2tt_mStop-675to800_mLSP-300to700_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2tt_2J_6 = kreator.makeMCComponent('T2tt_2J_6', '/SMS-8TeV-Pythia6Z_T2tt_mStop-500to800_mLSP-1/Summer12-START52_V9_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)
T2tt_2J_7 = kreator.makeMCComponent('T2tt_2J_7', '/SMS-8TeV-Pythia6Z_T2tt_mStop-150to475_mLSP-1/Summer12-START52_V9_FSIM-v1/AODSIM/V5/'+patNew,userName,filepattern)



T1tttt_2J = [ T1tttt_2J_1,T1tttt_2J_2,T1tttt_2J_3,T1tttt_2J_4,T1tttt_2J_5,T1tttt_2J_6,T1tttt_2J_7,T1tttt_2J_8 ]
T5VV_2J = [ T5VV_2J_1,T5VV_2J_2,T5VV_2J_3,T5VV_2J_4,T5VV_2J_5,T5VV_2J_6,T5VV_2J_7 ]
T2DegenerateStop_2J = [ T2DegenerateStop_2J_1, T2DegenerateStop_2J_2, T2DegenerateStop_2J_3, T2DegenerateStop_2J_4 ]
T2qq_2J = [ T2qq_2J_1, T2qq_2J_2, T2qq_2J_3, T2qq_2J_4 ]
T2bb_2J = [ T2bb_2J_1, T2bb_2J_2 ]
T2tt_2J = [ T2tt_2J_1, T2tt_2J_2, T2tt_2J_3, T2tt_2J_4, T2tt_2J_5, T2tt_2J_6, T2tt_2J_7 ]

susySamples = T1tttt_2J + T5VV_2J + T2DegenerateStop_2J + T2qq_2J + T2bb_2J + T2tt_2J

####################################################################################################################
#-----------PRIVATE FAST SIM---------------

lowmllFiles = [ f.strip() for f in open("%s/src/CMGTools/TTHAnalysis/python/samples/fastSim-lowmll.txt" % os.environ['CMSSW_BASE'], "r") if "cmgTuple_518" in f ]
def _grep(x,l): return [ i for i in l if x in i ]
FastSim_TTGStarMM = kreator.makePrivateMCComponent('FastSim_TTGStarMM',  '/store/caf/user/gpetrucc/ttH/gen/2013-05-23/ttgstar_lowmll_mumu_v2', _grep('ttgstar_lowmll_mumu_v2', lowmllFiles) )
FastSim_TTGStarEE = kreator.makePrivateMCComponent('FastSim_TTGStarEE',  '/store/caf/user/gpetrucc/ttH/gen/2013-05-23/ttgstar_lowmll_ee_v2', _grep('ttgstar_lowmll_ee_v2', lowmllFiles) )
FastSim_TTGStarTT = kreator.makePrivateMCComponent('FastSim_TTGStarTT',  '/store/caf/user/gpetrucc/ttH/gen/2013-05-23/ttgstar_lowmll_tautau', _grep('ttgstar_lowmll_tautau', lowmllFiles) )

lmutauFiles = [ f.strip() for f in open("%s/src/CMGTools/TTHAnalysis/python/samples/fastSim-lmutau.txt" % os.environ['CMSSW_BASE'], "r") if "cmgTuple" in f ]
S3m_m100_g050 = kreator.makePrivateMCComponent('S3m_m100_g050', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m100_g050', _grep('S3m_m100_g050', lmutauFiles))
S3m_m105_g052 = kreator.makePrivateMCComponent('S3m_m105_g052', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m105_g052', _grep('S3m_m105_g052', lmutauFiles))
S3m_m110_g055 = kreator.makePrivateMCComponent('S3m_m110_g055', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m110_g055', _grep('S3m_m110_g055', lmutauFiles))
S3m_m115_g057 = kreator.makePrivateMCComponent('S3m_m115_g057', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m115_g057', _grep('S3m_m115_g057', lmutauFiles))
S3m_m120_g060 = kreator.makePrivateMCComponent('S3m_m120_g060', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m120_g060', _grep('S3m_m120_g060', lmutauFiles))
S3m_m125_g062 = kreator.makePrivateMCComponent('S3m_m125_g062', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m125_g062', _grep('S3m_m125_g062', lmutauFiles))
S3m_m130_g065 = kreator.makePrivateMCComponent('S3m_m130_g065', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m130_g065', _grep('S3m_m130_g065', lmutauFiles))
S3m_m140_g070 = kreator.makePrivateMCComponent('S3m_m140_g070', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m140_g070', _grep('S3m_m140_g070', lmutauFiles))
S3m_m150_g075 = kreator.makePrivateMCComponent('S3m_m150_g075', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m150_g075', _grep('S3m_m150_g075', lmutauFiles))
S3m_m160_g080 = kreator.makePrivateMCComponent('S3m_m160_g080', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m160_g080', _grep('S3m_m160_g080', lmutauFiles))
S3m_m170_g085 = kreator.makePrivateMCComponent('S3m_m170_g085', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m170_g085', _grep('S3m_m170_g085', lmutauFiles))
S3m_m180_g090 = kreator.makePrivateMCComponent('S3m_m180_g090', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m180_g090', _grep('S3m_m180_g090', lmutauFiles))
S3m_m190_g095 = kreator.makePrivateMCComponent('S3m_m190_g095', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m190_g095', _grep('S3m_m190_g095', lmutauFiles))
S3m_m200_g100 = kreator.makePrivateMCComponent('S3m_m200_g100', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m200_g100', _grep('S3m_m200_g100', lmutauFiles))
S3m_m225_g112 = kreator.makePrivateMCComponent('S3m_m225_g112', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m225_g112', _grep('S3m_m225_g112', lmutauFiles))
S3m_m250_g125 = kreator.makePrivateMCComponent('S3m_m250_g125', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m250_g125', _grep('S3m_m250_g125', lmutauFiles))
S3m_m275_g137 = kreator.makePrivateMCComponent('S3m_m275_g137', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m275_g137', _grep('S3m_m275_g137', lmutauFiles))
S3m_m300_g150 = kreator.makePrivateMCComponent('S3m_m300_g150', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m300_g150', _grep('S3m_m300_g150', lmutauFiles))
S3m_m325_g162 = kreator.makePrivateMCComponent('S3m_m325_g162', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m325_g162', _grep('S3m_m325_g162', lmutauFiles))
S3m_m350_g175 = kreator.makePrivateMCComponent('S3m_m350_g175', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m350_g175', _grep('S3m_m350_g175', lmutauFiles))
S3m_m50_g025 = kreator.makePrivateMCComponent('S3m_m50_g025', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m50_g025', _grep('S3m_m50_g025', lmutauFiles))
S3m_m55_g027 = kreator.makePrivateMCComponent('S3m_m55_g027', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m55_g027', _grep('S3m_m55_g027', lmutauFiles))
S3m_m60_g030 = kreator.makePrivateMCComponent('S3m_m60_g030', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m60_g030', _grep('S3m_m60_g030', lmutauFiles))
S3m_m65_g032 = kreator.makePrivateMCComponent('S3m_m65_g032', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m65_g032', _grep('S3m_m65_g032', lmutauFiles))
S3m_m70_g035 = kreator.makePrivateMCComponent('S3m_m70_g035', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m70_g035', _grep('S3m_m70_g035', lmutauFiles))
S3m_m75_g037 = kreator.makePrivateMCComponent('S3m_m75_g037', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m75_g037', _grep('S3m_m75_g037', lmutauFiles))
S3m_m80_g040 = kreator.makePrivateMCComponent('S3m_m80_g040', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m80_g040', _grep('S3m_m80_g040', lmutauFiles))
S3m_m85_g042 = kreator.makePrivateMCComponent('S3m_m85_g042', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m85_g042', _grep('S3m_m85_g042', lmutauFiles))
S3m_m90_g045 = kreator.makePrivateMCComponent('S3m_m90_g045', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m90_g045', _grep('S3m_m90_g045', lmutauFiles))
S3m_m95_g047 = kreator.makePrivateMCComponent('S3m_m95_g047', '/store/cmst3/user/gpetrucc/lmutau/v1/S3m_m95_g047', _grep('S3m_m95_g047', lmutauFiles))
S4m_m100_g050 = kreator.makePrivateMCComponent('S4m_m100_g050', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m100_g050', _grep('S4m_m100_g050', lmutauFiles))
S4m_m105_g052 = kreator.makePrivateMCComponent('S4m_m105_g052', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m105_g052', _grep('S4m_m105_g052', lmutauFiles))
S4m_m110_g055 = kreator.makePrivateMCComponent('S4m_m110_g055', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m110_g055', _grep('S4m_m110_g055', lmutauFiles))
S4m_m115_g057 = kreator.makePrivateMCComponent('S4m_m115_g057', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m115_g057', _grep('S4m_m115_g057', lmutauFiles))
S4m_m120_g060 = kreator.makePrivateMCComponent('S4m_m120_g060', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m120_g060', _grep('S4m_m120_g060', lmutauFiles))
S4m_m125_g062 = kreator.makePrivateMCComponent('S4m_m125_g062', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m125_g062', _grep('S4m_m125_g062', lmutauFiles))
S4m_m130_g065 = kreator.makePrivateMCComponent('S4m_m130_g065', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m130_g065', _grep('S4m_m130_g065', lmutauFiles))
S4m_m140_g070 = kreator.makePrivateMCComponent('S4m_m140_g070', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m140_g070', _grep('S4m_m140_g070', lmutauFiles))
S4m_m150_g075 = kreator.makePrivateMCComponent('S4m_m150_g075', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m150_g075', _grep('S4m_m150_g075', lmutauFiles))
S4m_m160_g080 = kreator.makePrivateMCComponent('S4m_m160_g080', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m160_g080', _grep('S4m_m160_g080', lmutauFiles))
S4m_m170_g085 = kreator.makePrivateMCComponent('S4m_m170_g085', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m170_g085', _grep('S4m_m170_g085', lmutauFiles))
S4m_m180_g090 = kreator.makePrivateMCComponent('S4m_m180_g090', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m180_g090', _grep('S4m_m180_g090', lmutauFiles))
S4m_m190_g095 = kreator.makePrivateMCComponent('S4m_m190_g095', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m190_g095', _grep('S4m_m190_g095', lmutauFiles))
S4m_m200_g100 = kreator.makePrivateMCComponent('S4m_m200_g100', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m200_g100', _grep('S4m_m200_g100', lmutauFiles))
S4m_m225_g112 = kreator.makePrivateMCComponent('S4m_m225_g112', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m225_g112', _grep('S4m_m225_g112', lmutauFiles))
S4m_m250_g125 = kreator.makePrivateMCComponent('S4m_m250_g125', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m250_g125', _grep('S4m_m250_g125', lmutauFiles))
S4m_m275_g137 = kreator.makePrivateMCComponent('S4m_m275_g137', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m275_g137', _grep('S4m_m275_g137', lmutauFiles))
S4m_m300_g150 = kreator.makePrivateMCComponent('S4m_m300_g150', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m300_g150', _grep('S4m_m300_g150', lmutauFiles))
S4m_m325_g162 = kreator.makePrivateMCComponent('S4m_m325_g162', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m325_g162', _grep('S4m_m325_g162', lmutauFiles))
S4m_m350_g175 = kreator.makePrivateMCComponent('S4m_m350_g175', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m350_g175', _grep('S4m_m350_g175', lmutauFiles))
S4m_m50_g025 = kreator.makePrivateMCComponent('S4m_m50_g025', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m50_g025', _grep('S4m_m50_g025', lmutauFiles))
S4m_m55_g027 = kreator.makePrivateMCComponent('S4m_m55_g027', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m55_g027', _grep('S4m_m55_g027', lmutauFiles))
S4m_m60_g030 = kreator.makePrivateMCComponent('S4m_m60_g030', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m60_g030', _grep('S4m_m60_g030', lmutauFiles))
S4m_m65_g032 = kreator.makePrivateMCComponent('S4m_m65_g032', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m65_g032', _grep('S4m_m65_g032', lmutauFiles))
S4m_m70_g035 = kreator.makePrivateMCComponent('S4m_m70_g035', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m70_g035', _grep('S4m_m70_g035', lmutauFiles))
S4m_m75_g037 = kreator.makePrivateMCComponent('S4m_m75_g037', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m75_g037', _grep('S4m_m75_g037', lmutauFiles))
S4m_m80_g040 = kreator.makePrivateMCComponent('S4m_m80_g040', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m80_g040', _grep('S4m_m80_g040', lmutauFiles))
S4m_m85_g042 = kreator.makePrivateMCComponent('S4m_m85_g042', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m85_g042', _grep('S4m_m85_g042', lmutauFiles))
S4m_m90_g045 = kreator.makePrivateMCComponent('S4m_m90_g045', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m90_g045', _grep('S4m_m90_g045', lmutauFiles))
S4m_m95_g047 = kreator.makePrivateMCComponent('S4m_m95_g047', '/store/cmst3/user/gpetrucc/lmutau/v1/S4m_m95_g047', _grep('S4m_m95_g047', lmutauFiles))
LMuTau = [ S3m_m100_g050, S3m_m105_g052, S3m_m110_g055, S3m_m115_g057, S3m_m120_g060, S3m_m125_g062, S3m_m130_g065, S3m_m140_g070, S3m_m150_g075, S3m_m160_g080, S3m_m170_g085, S3m_m180_g090, S3m_m190_g095, S3m_m200_g100, S3m_m225_g112, S3m_m250_g125, S3m_m275_g137, S3m_m300_g150, S3m_m325_g162, S3m_m350_g175, S3m_m50_g025, S3m_m55_g027, S3m_m60_g030, S3m_m65_g032, S3m_m70_g035, S3m_m75_g037, S3m_m80_g040, S3m_m85_g042, S3m_m90_g045, S3m_m95_g047, S4m_m100_g050, S4m_m105_g052, S4m_m110_g055, S4m_m115_g057, S4m_m120_g060, S4m_m125_g062, S4m_m130_g065, S4m_m140_g070, S4m_m150_g075, S4m_m160_g080, S4m_m170_g085, S4m_m180_g090, S4m_m190_g095, S4m_m200_g100, S4m_m225_g112, S4m_m250_g125, S4m_m275_g137, S4m_m300_g150, S4m_m325_g162, S4m_m350_g175, S4m_m50_g025, S4m_m55_g027, S4m_m60_g030, S4m_m65_g032, S4m_m70_g035, S4m_m75_g037, S4m_m80_g040, S4m_m85_g042, S4m_m90_g045, S4m_m95_g047 ]


fastSimSamples = [ FastSim_TTGStarMM, FastSim_TTGStarEE, FastSim_TTGStarTT ] + LMuTau


mcSamples=mcSamples_1+mcSamples_2+mcSamples_3 
mcSamplesAll = mcSamples+mcSamples_4+susySamples+fastSimSamples

#-----------DATA---------------

dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"
#lumi: 12.21+7.27+0.134 = 19.62 /fb @ 8TeV

json=dataDir+'/json/Cert_Run2012ABCD_22Jan2013ReReco.json'

DoubleMuAB = cfg.DataComponent(
    name = 'DoubleMuAB',
    files = getFiles('/DoubleMu/Run2012A-22Jan2013-v1/AOD/'+patPF,userName,filepattern)+ \
            getFiles('/DoubleMuParked/Run2012B-22Jan2013-v1/AOD/'+patPF,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

DoubleMuC = cfg.DataComponent(
    name = 'DoubleMuC',
    files = getFiles('/DoubleMuParked/Run2012C-22Jan2013-v1/AOD/'+patPF,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

DoubleMuD = cfg.DataComponent(
    name = 'DoubleMuD',
    files = getFiles('/DoubleMuParked/Run2012D-22Jan2013-v1/AOD/'+patPF,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

DoubleElectronAB = cfg.DataComponent(
    name = 'DoubleElectronAB',
    files = getFiles('/DoubleElectron/Run2012A-22Jan2013-v1/AOD/'+patPF,userName,filepattern)+ \
            getFiles('/DoubleElectron/Run2012B-22Jan2013-v1/AOD/'+patPF,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

DoubleElectronC = cfg.DataComponent(
    name = 'DoubleElectronC',
    files = getFiles('/DoubleElectron/Run2012C-22Jan2013-v1/AOD/'+patPF,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

DoubleElectronD = cfg.DataComponent(
    name = 'DoubleElectronD',
    files = getFiles('/DoubleElectron/Run2012D-22Jan2013-v1/AOD/'+patPF,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

MuEGAB = cfg.DataComponent(
    name = 'MuEGAB',
    files = getFiles('/MuEG/Run2012A-22Jan2013-v1/AOD/'+patNew,userName,filepattern)+ \
            getFiles('/MuEG/Run2012B-22Jan2013-v1/AOD/'+patNew,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

MuEGC = cfg.DataComponent(
    name = 'MuEGC',
    files = getFiles('/MuEG/Run2012C-22Jan2013-v1/AOD/'+patNew,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

MuEGD = cfg.DataComponent(
    name = 'MuEGD',
    files = getFiles('/MuEG/Run2012D-22Jan2013-v1/AOD/'+patNew,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

SingleMuAB = cfg.DataComponent(
    name = 'SingleMuAB',
    files = getFiles('/SingleMu/Run2012A-22Jan2013-v1/AOD/'+patPF,userName,filepattern)+ \
            getFiles('/SingleMu/Run2012B-22Jan2013-v1/AOD/'+patPF,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

SingleMuC = cfg.DataComponent(
    name = 'SingleMuC',
    files = getFiles('/SingleMu/Run2012C-22Jan2013-v1/AOD/'+patPF,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

SingleMuD = cfg.DataComponent(
    name = 'SingleMuD',
    files = getFiles('/SingleMu/Run2012D-22Jan2013-v1/AOD/'+patPF,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

SingleElectronAB = cfg.DataComponent(
    name = 'SingleElectronAB',
    files = getFiles('/SingleElectron/Run2012A-22Jan2013-v1/AOD/'+patOld,userName,filepattern)+ \
            getFiles('/SingleElectron/Run2012B-22Jan2013-v1/AOD/'+patOld,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

SingleElectronC = cfg.DataComponent(
    name = 'SingleElectronC',
    files = getFiles('/SingleElectron/Run2012C-22Jan2013-v1/AOD/'+patOld,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

SingleElectronD = cfg.DataComponent(
    name = 'SingleElectronD',
    files = getFiles('/SingleElectron/Run2012D-22Jan2013-v1/AOD/'+patOld,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

METAB = cfg.DataComponent(
    name = 'METAB',
    files = getFiles('/MET/Run2012A-22Jan2013-v1/AOD/'+patNew,userName,filepattern)+ \
            getFiles('/MET/Run2012B-22Jan2013-v1/AOD/'+patNew,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

METC = cfg.DataComponent(
    name = 'METC',
    files = getFiles('/MET/Run2012C-22Jan2013-v1/AOD/'+patNew,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )

METD = cfg.DataComponent(
    name = 'METD',
    files = getFiles('/METParked/Run2012D-22Jan2013-v1/AOD/'+patNew,userName,filepattern),
    intLumi = 1,
    triggers = [],
    json = json
    )




   
#   ####################################################################################################################
#   
#             
dataSamplesMu=[DoubleMuAB,DoubleMuC,DoubleMuD]
dataSamplesE=[DoubleElectronAB,DoubleElectronC,DoubleElectronD]
dataSamplesMuE=[MuEGAB,MuEGC,MuEGD]
dataSamples2L = dataSamplesMu+dataSamplesE+dataSamplesMuE
dataSamples1Mu=[SingleMuAB,SingleMuC,SingleMuD]
dataSamples1E=[SingleElectronAB,SingleElectronC,SingleElectronD]
dataSamplesMET=[METAB,METC,METD]
dataSamplesAll = dataSamples2L+dataSamples1Mu+dataSamples1E+dataSamplesMET

from CMGTools.TTHAnalysis.setup.Efficiencies import eff2012


#Define splitting
for comp in mcSamplesAll:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250 if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012
# redefine some splittings
for C in [DYJetsM50,TTJetsLep,TTJetsSem,TTJetsSem2,TTLep,DY1JetsM50]:
    C.splitFactor = 500
for comp in fastSimSamples:
    comp.splitFactor = 10
for comp in LMuTau:
    comp.splitFactor = 2

for comp in dataSamplesMu:
    comp.splitFactor = 800
    comp.isMC = False
    comp.isData = True

for comp in dataSamplesE:
    comp.splitFactor = 800
    comp.isMC = False
    comp.isData = True
    
for comp in dataSamplesMuE:
    comp.splitFactor = 400
    comp.isMC = False
    comp.isData = True

for comp in dataSamples1Mu:
    comp.splitFactor = 500
    comp.isMC = False
    comp.isData = True



