---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

# <i class="fas fa-user" aria-hidden="true"></i>About Me {#about-me}

I am an AI Research Engineer at [MBZUAI](https://mbzuai.ac.ae/), working with [Prof. Salman Khan](https://salman-h-khan.github.io/) on multimodal foundation models and agentic AI for climate analysis ([Climate Co-Pilot](https://mbzuai-oryx.github.io/ClimateCoPilot/)). Previously, I was with the BioMedIA Lab at MBZUAI under [Prof. Mohammad Yaqub](https://scholar.google.co.uk/citations?user=9dfn5GkAAAAJ), first as an M.Sc. student in Computer Vision and then as a Graduate Research Assistant. My work there covered echocardiography, fetal ultrasound, and brain tumor segmentation, including [FetalCLIP](https://biomedia-mbzuai.github.io/FetalCLIP/), a vision-language foundation model for fetal ultrasound.

In 2025, I worked as a Senior Data Scientist at [Miral Experiences](https://miral.ae/miralexperiences/) in Abu Dhabi, transforming park data into business insights and recommendations, from personalized recommendations for visitors across four parks and price recommendation systems for retail and F&B to advanced ad hoc analytics for business leaders. Across research and industry, I enjoy taking a problem from careful data curation through modeling to a solution that people can use and build upon.

I am always happy to hear from researchers and teams working on related problems, so please feel free to reach out by [email](mailto:fadillahadam11@gmail.com). To give my current commitments the focus they deserve, I am unfortunately not able to take on any part-time roles at the moment.

**Research interests:** multimodal models, foundation models, agentic AI, AI for healthcare, AI for climate, and applied AI & ML.

<p class="gs-cites" id="gs-cites" hidden><a href="https://scholar.google.com/citations?user=W-4975wAAAAJ"><i class="ai ai-google-scholar" aria-hidden="true"></i> Google Scholar citations: <strong id="total_cit"></strong></a></p>


# <i class="fas fa-newspaper" aria-hidden="true"></i>News {#news}

{% include news.html %}


# <i class="fas fa-book-open" aria-hidden="true"></i>Selected Publications {#selected-publications}

The full list of publications is available on [Google Scholar](https://scholar.google.com/citations?user=W-4975wAAAAJ).

<!--
  Per-paper citation counts are filled in from the Google Scholar crawler data.
  data='...' is the paper's Scholar ID: the value after "citation_for_view=" on its Scholar page.
-->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">npj Digit. Med. 2026</div><img src='images/teasers/fetalclip.png' alt="FetalCLIP dataset curation and pretraining overview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[FetalCLIP: A Visual-Language Foundation Model for Fetal Ultrasound Image Analysis](https://doi.org/10.1038/s41746-026-02907-9)

**F. A. Maani**<span class="eq" title="Equal contribution">*</span>, N. Saeed<span class="eq" title="Equal contribution">*</span>, T. Saleem, Z. Farooq, H. Alasmawi, W. Diehl, A. Mohammad, G. Waring, S. Valappil, L. Bricker, M. Yaqub

*npj Digital Medicine*, 2026

[**Paper**](https://doi.org/10.1038/s41746-026-02907-9) \| [**Project**](https://biomedia-mbzuai.github.io/FetalCLIP/) \| [**Code**](https://github.com/biomedia-mbzuai/fetalclip) <strong><span class='show_paper_citations' data='W-4975wAAAAJ:UebtZRa9Y70C'></span></strong>

- A vision-language foundation model for fetal ultrasound, pretrained on over 210K image–caption pairs and evaluated on plane classification, gestational age estimation, congenital heart defect detection, and segmentation.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='images/teasers/earthalign.png' alt="EarthAlign dataset overview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EarthAlign: Learning Language-Aligned Representations of Earth System Data](https://arxiv.org/abs/2610.14624)

**F. A. Maani**, N. Saeed, J. Ma, D. T. Nguyen, Y. Wehbe, D. Watson-Parris, S. Khan

*arXiv preprint*, 2026

[**arXiv**](https://arxiv.org/abs/2610.14624) \| [**Project**](https://mbzuai-oryx.github.io/EarthAlign/) \| [**Code**](https://github.com/mbzuai-oryx/EarthAlign) \| [**Dataset & Weights**](https://huggingface.co/datasets/MBZUAI/EarthAlign) <strong><span class='show_paper_citations' data='W-4975wAAAAJ:4TOpqqG69KYC'></span></strong>

- A 553K-sample dataset pairing natural-event and normal-weather records with ERA5 meteorological data and grounded captions, plus MeteoLIP, a dual-encoder model for meteorology–language alignment.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='images/teasers/dark.png' alt="DARK framework overview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DARK: Diagonal-Anchored Repulsive Knowledge Distillation for Vision-Language Models under Extreme Compression](https://arxiv.org/abs/2603.05421)

N. Saeed, A. Hanif, **F. A. Maani**, H. Alasmawi, M. Yaqub

*arXiv preprint*, 2026

[**arXiv**](https://arxiv.org/abs/2603.05421) \| [**Project**](https://www.numansaeed.com/dark/) \| [**Code**](https://github.com/numanai/MobileFetalCLIP) <strong><span class='show_paper_citations' data='W-4975wAAAAJ:Zph67rFs4hoC'></span></strong>

- A contrastive distillation method that compresses FetalCLIP into MobileFetalCLIP, with a 26× smaller visual encoder that runs in 1.6 ms on an iPhone 16 Pro while matching or exceeding its teacher on zero-shot benchmarks.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MICCAI 2024 (Oral)</div><img src='images/teasers/coreecho.png' alt="CoReEcho embedding comparison" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CoReEcho: Continuous Representation Learning for 2D+time Echocardiography Analysis](https://doi.org/10.1007/978-3-031-72083-3_55)

**F. A. Maani**, N. Saeed, A. Matsun, M. Yaqub

*Medical Image Computing and Computer Assisted Intervention (MICCAI)*, 2024

[**Paper**](https://papers.miccai.org/miccai-2024/paper/2916_paper.pdf) \| [**Code**](https://github.com/BioMedIA-MBZUAI/CoReEcho) <strong><span class='show_paper_citations' data='W-4975wAAAAJ:Y0pCki6q_DkC'></span></strong>

- A training framework that learns continuous representations for direct ejection fraction regression, reaching state-of-the-art results on EchoNet-Dynamic and transferring better to smaller echocardiography datasets.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">UMB 2024</div><img src='images/teasers/simlvseg.png' alt="SimLVSeg method illustration" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SimLVSeg: Simplifying Left Ventricular Segmentation in 2-D+Time Echocardiograms with Self- and Weakly Supervised Learning](https://doi.org/10.1016/j.ultrasmedbio.2024.08.023)

**F. A. Maani**, A. Ukaye, N. Saadi, N. Saeed, M. Yaqub

*Ultrasound in Medicine & Biology*, 2024

[**Paper**](https://doi.org/10.1016/j.ultrasmedbio.2024.08.023) \| [**Code**](https://github.com/BioMedIA-MBZUAI/SimLVSeg) <strong><span class='show_paper_citations' data='W-4975wAAAAJ:ufrVoPGSRksC'></span></strong>

- Self-supervised temporal masking followed by weakly supervised training lets video networks segment the left ventricle from sparsely annotated echocardiograms, reaching 93.32% Dice on EchoNet-Dynamic.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">BrainLes 2023</div><img src='images/teasers/brats2023.png' alt="BraTS 2023 qualitative segmentation results" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Advanced Tumor Segmentation in Medical Imaging: An Ensemble Approach for BraTS 2023 Adult Glioma and Pediatric Tumor Tasks](https://arxiv.org/abs/2403.09262)

**F. A. Maani**<span class="eq" title="Equal contribution">*</span>, A. U. R. Hashmi<span class="eq" title="Equal contribution">*</span>, M. Aljuboory, N. Saeed, I. Sobirov, M. Yaqub

*BrainLes Workshop @ MICCAI*, 2023

[**arXiv**](https://arxiv.org/abs/2403.09262) <strong><span class='show_paper_citations' data='W-4975wAAAAJ:IjCSPb-OGe4C'></span></strong>

- An ensemble of SegResNet and MedNeXt with lesion-wise post-processing, placing 3rd in the BraTS 2023 Adult Glioma challenge.
</div>
</div>


# <i class="fas fa-briefcase" aria-hidden="true"></i>Experience {#experience}

### <i class="fas fa-flask" aria-hidden="true"></i>Research {#experience-research}

{% include cv-list.html items=site.data.experience.research %}

### <i class="fas fa-building" aria-hidden="true"></i>Industry {#experience-industry}

{% include cv-list.html items=site.data.experience.industry %}


# <i class="fas fa-trophy" aria-hidden="true"></i>Honors and Awards {#honors-and-awards}

{% include cv-list.html items=site.data.honors variant="compact" %}


# <i class="fas fa-graduation-cap" aria-hidden="true"></i>Education {#education}

{% include cv-list.html items=site.data.education %}
