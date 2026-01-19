---
layout: default
title: Draft Business Case
crumbs:
  - link: /ospo/business-case
    text: "Draft Business Case for UCL's Open Source Programme Office"
---


# UCL's Open Source Programme Office

*Executive Summary*
> help them understand the project’s purpose, benefits and implications. Some components of an executive summary include the project overview, business need, proposed solution to the need, cost estimate, return on investment, risks, timeline and a call to action.


Our university as many institutions and organisations around the globe depends on Open Source,
whether it's software, hardware, data or other resources as research and educational outputs.
Open source software is everywhere and it has a huge economic impact.
The [State of Open Source paper][sospaper], shows that 96% of all software included open source software.
Moreover, a [study from the Harvard Business School][harvard-oss] has shown recently that open source software generated $8.8 trillion of value and production costs are reduced a factor of 3.5.
Other open source "products" haven't been under such a detailed analysis yet, however, from the point of view of an university,
they are still very important, for example for the Open Science reproducibility mission as well as for the creation of Open Educational resources.

The creation of an Open Source Programme Office (OSPO) helps to coordinate its usage and development as well as to nurture its adoption across the university.
We propose three main pillars that an OSPO in UCL should cover: Research, Education and Infrastructure,
supported by three main foundations: Training, Community and Policy.
With those six aspects we are increasing collaboration and visibility (within and outside UCL) as well as providing an overview about the stronger and weakest points of our ecosystem and dependencies.
This office will provide a service to obtain metrics, deliver training and provide mentorship and guidance on running open source projects;
a medium to support grant applications and compliance with respect to open source requirements;
a hub of communication between the UCL community, innovation and enterprise team and external partners;
and an advocacy platform for promoting open source culture practices and provide policy recommendations across the university.
To be able to offer all this, we propose to build on above what [UCL's Advanced Research Computing Centre][arc] (ARC) and [UCL Office for Open Science and Scholarship][OOSS] has created
and add components through out the next five years,
with costs shared across different departments across UCL,
starting with the current 0.25 FTE provided by ARC and increase it to a shared 3 FTE across the university at the end of this period.

Being the first UK university to have an OSPO provides a service no available in the country to our researchers, staff and students,
as well as brings visibility in open source communities, attracting workforce and students, as well as investment from external bodies.


[sospaper]: https://www.synopsys.com/software-integrity/resources/analyst-reports/open-source-security-risk-analysis.html#introMenu
[harvard-oss]: http://dx.doi.org/10.2139/ssrn.4693148
[arc]: https://www.ucl.ac.uk/arc
[OOSS]: https://www.ucl.ac.uk/library/open-science-research-support/ucl-office-open-science-and-scholarship

## Context

> context for your project, explaining the problem that it's meant to solve and how it aligns with the organisation's vision and strategic plan

UCL has a long history of open-source software development for research and open-source educational resources.

In a recent study, we identified more than a thousand open-source software projects owned[^owned] by the UCL community that are directly related to UCL research, publications, or teaching on the GitHub platform.
The oldest[^oldest] of these projects dates back to 1997, notably before the invention of git itself[^?Do people know what's git], and is still one of our most active projects today.

We know that UCL has given birth to open source communities such as the [Open Street Map][osm][^osmap-ucl], which was supported and hosted by UCL from 2004 when it was created, to at least 2008. This platform has been providing open-source licensed map data free to use, to edit and distribute, to everyone, being used by lots of mapping applications, transport companies, government agencies, humanitarian organisations, news sites and websites[^osm-companies].
A more recent example is the [BrainGlobe Initiative][bgi] that was established between researches at the Sainsbury Wellcome Centre and the Technical University of Munich since 2XXX(FIXME). They have developed a whole ecosystem of research software tools and nurture a community of researcher over the years, that was, last year, recognised by receiving an international award for its contribution to open, accessible and collaborative neuroscience[^bgi-award]. 

Those are only three examples, but we are sure that there are many others that we don't know within UCL. As researchers have become more familiar with the benefits of open source development, as well as, funding bodies around the world, have started to request to open source what is created with public money, at ARC we've seen an increase of researchers being interested to follow those practice.

Open source projects enables collaboration and discoverability, however, open source projects also suffer from support and most of the times it relies on volunteering efforts. As a organisation that uses and produces open source, we should be more aware of our production and dependencies and how to support them better.
This is the main objective of the Open Source Programme Office we propose. Mapping and cataloguing all the open source we generate helps us to have an overview of where are the needs for our community, and therefore act on it. <!-- Through training, guidance, collaborating, lobbing,  -->

This problem is commonly represented by this xkcd.com webcomic by Randall Munroe, where it represents the fragility of the digital infrastructure.

<center>

**Dependency**

![XKCD comic strip showing a structure form by blocks one on top of each other. With the text on top saying "All modern digital infrastructure". In the bottom right there's a small block that give support to the whole structure above. That's got a text saying "A project some random person in Nebraska has been thanklessly maintaining since 2003".](https://imgs.xkcd.com/comics/dependency_2x.png "Someday ImageMagick will finally break for good and we'll have a long period of scrambling as we try to reassemble civilization from the rubble.")

*Figure 1: [Dependency comic strip from xkcd.com][xkcd-dep]. Licensed as CC-by-NC*

</center>

<!-- UCL vision + strategic plan. (ARC + OOSS) -->
As the [Advanced Research Computing Centre (ARC)][arc] has led nationally the creation of research software engineering (and other digital research professional) roles within the sector, 
and the [Office of Open Science and Scholarship][OOSS] has promoted the adoption of open practices and approaches across universities, 
this puts UCL at an exceptional position to provide the support that Open Source needs across all the layers in the university and be in the forefront of open source within the UK.

<!-- Footnotes -->
[^owned]: Where "owned" simply denotes project ownership: open source development work done by UCL staff in aid of UCL research or education.
[^oldest]: [STIR](https://github.com/UCL/STIR) - The Software for Tomographic Image Reconstruction.
[^osmap-ucl]: [Open Street Map][osm] is a crowdsourced mapping platform initiated in [2004 at UCL][osmapref] by Steve Coast at CASA
[^osm-companies]: [Open Street Map list of prominent users][osmap-users] list also some universities, but unfortunately not UCL.
[^bgi-award]: The 2025 International Prize by the Neuro-Irv and Helga Cooper Foundation Open Science Prizes Selection Committee is organised by The Tanenbaum Open Science Institute. More information in [Sainbury Wellcome Centre press release][swc-pr].
<!-- End Footnotes -->

<!-- links -->
[osm]: https://www.openstreetmap.org/
[osmapref]: https://discovery.ucl.ac.uk/id/eprint/13849/1/13849.pdf
[osmap-users]: https://welcome.openstreetmap.org/about-osm-community/consumers/
[bgi]: https://brainglobe.info/about.HTML
[swc-pr]: https://www.sainsburywellcome.org/web/research-news/brainglobe-initiative-wins-2025-international-prize
[xkcd-dep]: https://xkcd.com/2347/
<!-- end links -->

## What is an OSPO?

An Open Source Programme Office (OSPO) is a body within an organisation to look after its open source strategy and operations. OSPOs have been widely adopted in the commercial world[^OSPO-commerce], governmental institutions and world organisations[^OSPO-public]. More recently, various academic and research institutions have also found the value of having OSPOs. Focusing on the latest, we can find research centres such as [CERN][ospo-cern] or [Space Telescope Science Institute][ospo-stsci] and universities like [Johns Hopkins][ospo-jhu] (the first one, since 2019), [University of California][ospo-uc] and [Carnegie Mellon University][ospo-cmu] in the USA, or European examples like [Trinity College Dublin][ospo-tcd] in Ireland, [University of Luxembourg][ospo-snt], and [ETH Zurich][ospo-eth] in Switzerland.

<!-- Footnotes -->
[^OSPO-commerce]: The two biggest OSPO networks in industry are: [OSPO Alliance][ospo-alliance] supported by the [Eclipse Foundation][eclipse] and [TODO Group][ospo-todogrp] supported by the [Linux Foundation][LF]. A [report published in 2024 by the TODO Group][state-of-ospo-2024] found that 77% of large organisations have an OSPO (DOI: 10.70828/FXMR3018). <!-- typos: ignore -->
[^OSPO-public]: Covering this space there is the [EU OSPO Network][ospo-eu] led by the [EC OSPO][ospo-ec], and the [Public Sector OSPOs Network][ospo-public]. They include OSPOs from the [United Nations][ospo-un]; country-wide examples like the [French government][ospo-fr] or the [Netherlands](https://opensourcewerken.nl/); cities such as [City of Paris][ospo-paris] or [Munich][ospo-munich]; and specialised public organisations like [Digital Service at the Centers for Medicare and Medicaid Services in US][ospo-cms].
<!-- End Footnotes -->

Though the goals of organisations across these domains differ when establishing an OSPO, they create a fabric that helps those organisations to collaborate and combine efforts to maximise the impact (and support) of open source software. Some activities that an OSPO may do are:

- To advocate for Open Source practises between an organisation through community engagement;
- To measure usage of and dependency on open (and closed!) source projects;
- To measure the organisation's impact on open source;
- To mitigate associate risks (unlicensed code, closed source, etc);
- To promote, guide and educate internal and external community members on open source culture from technical, social, political and economic perspectives;
- To push policy forward that safeguards open source and protects technological sovereignty of the institution.

![](./Activities-of-academic-OSPO.png)
*Figure 1: Activities of an Academic OSPO - From [Young, et al. (2024)][young-2024] - Licensed under CC-BY*

Those activities, however, are not new to OSPOs. Over the years, different groups within organisations have been engaging in some of those activities. For example, Oxford University had a group named [OSS Watch][oss-watch] between 2003-2014 that provided unbiased advice and guidance on the use, development, and licensing of free software, open source software, and open source hardware. Similarly, the [Software Sustainability Institute][ssi] has been advocating for better software practices in research across the UK since 2010.

A more detailed definition of an academic OSPO can be found in [Young, et al. (2024)][young-2024]

[LF]: https://www.linuxfoundation.org/
[eclipse]: https://www.eclipse.org/
[ospo-alliance]: https://ospo-alliance.org/
[ospo-cern]: https://opensource.web.cern.ch/
[ospo-cms]: https://cms.gov/digital-service/open-source-program-office
[ospo-cmu]: https://www.library.cmu.edu/services/ospo
[ospo-ec]: https://interoperable-europe.ec.europa.eu/collection/ec-ospo
[ospo-eth]: https://transfer.ethz.ch/researchers/oss.html
[ospo-eu]: https://static-page-bdf202.usercontent.opencode.de/
[ospo-fr]: https://code.gouv.fr/
[ospo-jhu]: https://ospo.library.jhu.edu/
[ospo-munich]: https://opensource.muenchen.de/ospo.html
[ospo-paris]: https://opensource.paris.fr/
[ospo-public]: https://floss-pso.network/
[ospo-snt]: https://www.uni.lu/snt-en/
<!-- FIXME: STSci appears on archived OSPO++ page, but no link -->
[ospo-stsci]: http://www.stsci.edu/
[ospo-tcd]: https://www.tcd.ie/innovation/for-trinity-innovators/open-source-programme-office/
[ospo-todogrp]: https://todogroup.org/
[ospo-uc]: https://ucospo.net/
[ospo-un]: https://undp.org/digital
[oss-watch]: http://oss-watch.ac.uk/
[ssi]: https://www.software.ac.uk/
[state-of-ospo-2024]: https://www.linuxfoundation.org/research/ospo-2024
[young-2024]: https://doi.org/10.5281/zenodo.13910682

## Why does UCL need an OSPO? What benefits does it give?

Open Source is a fundamental component of our research and university infrastructure. However, this is usually forgotten and considered as a given. We do not know how much we depend on it. Equally, we know very little about the social, research, and economic impact that the open source code generated by UCL has. Contributing to Open Source projects requires more than technical knowledge, it is tied to social and economic aspects, and an OSPO helps to make it more accessible. An OSPO in UCL will benefit the following areas:

- research
  - Provide guidance on sustainability, community engagement and licensing.
- education
  - Train students and staff on the use of and contribution to Open Source projects.
  - Promote Open source alternatives to tools taught on courses to allow learners improve skills when losing access to closed source tools
- infrastructure (HPC, Moodle, Portico, HR & Finances, Department administration)
  - Provide support to open source tooling
  - Enable cross-department collaboration
- community
  - Ease collaboration with different institutions for similar tasks (from research software to infrastructure)
- policy
  - Include Open Source solutions and technical sovereignty into UCL procurement,
- impact
  - metrics - what's created within/with help from UCL, what are we depending on. Attract funding and collaborations
  - skills promoted will help students employment while also attract talent from open source communities
  - gain technical sovereignty


**mission statement** <!-- What and How; Doing now towards goals -->
> You’ll need to define your project vision, goals and objectives.

To support and train UCL community to reinforcing involvement and collaboration with open source communities, increasing students employability and strengthen industry links.

**vision** <!-- Why | meaning; Building towards the future -->

To establish UCL as a university that nurtures open source development supporting students and staff in their open source needs.

**goals**

- Identify projects that need support (internal and external);
- Train UCL members on open source technically and culturally;
- Promote open source infrastructure;
- Study impact of open source within the university;
- Collaborate with external communities and industry;
- Provide legal guidance on licensing and open source contributions.

**objectives**

<!-- what would be the difference between objectvies here and the one set under § Plan? -->


> *explain how it fits a niche or serves a need*
**Risks of not having an OSPO**
> What is the risk of not having one?

One of the biggest difficulties on large institutions is communication. And this is more aggravated when there's not a central hub.
In the case of open source, members of our community are mostly self-guided, having to rediscover all from scratch.
Not having one central hub of training and information on these topics mean keeping the statue quo and our community keeps reinventing rather than collaborating.

Additionally, publicly available and licensed reusable material is increasingly understood as a research output or project deliverables. This is being required and recognised by funding bodies as well as by excellence frameworks. Having an OSPO will help identify those while providing guidance on how to support the long-term sustainability of those outputs.

A major risk that an OSPO mitigates is a legal one.
One of the mandates of an OSPO is to develop an informed organisation-wide strategy for licensing open source projects and to provide guidance to developers and maintainers.
In our recent study, we noted 36.1% of UCL's open-source projects are unlicensed, meaning legally unusable by anyone.
While we also detected some projects violating licencing rules required. This could result on lawsuits and incur on costs.

Finally, there are also some financial risks,
without an OSPO, the university
may spend on closed source products when there are good and cheaper open source alternatives;
can fall into vendor lock-in leading to inability to pivot away from expensive contracts (at least without significant costs);
be locked-out in case of geopolitical circumstances[^icc-case];
take poor choices of open source solutions that lead to expensive failures or support costs.
Whereas if included open source metrics within the procurement process and help to support teams to develop the skills to maintain that software not just puts UCL in a better position, but it also contributes to improvements for users around the world and to the growth of the internal team.

<!-- footnotes -->
[^icc-case]: [Microsoft suspend access to email account to an International Criminal Court prosecutor][ms-icc] is a very recent case of situations that could arise when running most of our infrastructures on foreign companies.
<!-- end footnotes -->

<!-- links -->
[ms-icc]: https://www.nytimes.com/2025/06/20/technology/us-tech-europe-microsoft-trump-icc.html
<!-- endlinks -->

## How would it work at UCL?

An OSPO in UCL will become a team providing a central hub of communication, research, training and support, with different scopes. 
The team will be composed by a pool of staff and students from across the university and managed by a committee formed by delegates representing different aspect of the university (namely research, education, infrastructure, community, policy,services).
This support is expected to be provided in-kind by different departments (0.2-0.4FTE each). However, for certain projects and activities OSPO members will look for funding sources to accomplish them.

### Plan

*project definition*
> provide general information about your projects, such as the business objectives that will be achieved and the project plan outline. It offers a comprehensive overview of the project including its objectives and scope. Here, include details such as the objectives, stakeholders, scope, expected outcomes and constraints.

*project plan*
> Figure out the tasks you’ll have to take to get the project done. Estimate how long it will take to complete each one.

*risk assessment*
> identify and analyse the risks associated with your project activities. From there, you can assess the likelihood and impact of each and rank them based on this information. The risk assessment makes it easier to focus on the most pressing risks and includes a mitigation strategy to reduce the impact in case the risk comes to fruition.

#### Continue work

Through the past years, members of the proposed OSPO has been already providing some community support. These are expected to continue through out the following years.

Few members of the UCL have been participating on Summer of Code programmes such as Google's. We help to organise and advertise those through out the student community.

There are already communities that are related with open source across campus, such as Linux User Group, Latex User Group, Python Community of Practice, R Users, and various code clubs and student societies. The OSPO with support from ARC will continue supporting and promoting those community initiatives.

We are working with funding bodies and external stakeholders to promote Open Source, such as UKRI, DiRAC, Software Sustainability Institute. Helping to draft future policy and funding calls.

Continue to strength ties with international open source networks we are members from, such as the Community for University and Research Institution OSPOs ([CURIOSS][curioss]), the Community Health Analytics in Open Source Software ([CHAOSS][chaoss]) and the [High Performance Software foundation][hpsf], as well as support other UK universities that want to develop an OSPO.

#### Year 1

During the first year the OSPO will continue to maintain and augment the metrics analysis we started last year measuring all the open source software projects we learn about. Additionally, we will start to measure with external projects the UCL community contributes to. Impact reports will be published every six months from the data extracted.

The OSPO committee will be formed with the UCL staff who has already reached us, and as part of their commitment will be to define the membership terms and structure of this committee.

In collaboration with ARC education team, OSPO team will map and advertise on the web which programs, training and resources exists on the university that are providing training related with open source. 
For example, ARC's led [Centre for Doctoral Training in Collaborative Computational Modelling at the Interface][ccmi] has a strong emphasis on learning to contribute to open source communities.

Design, distribute and analyse a survey to understand the open source needs across the UCL community. 
The design will be based on surveys run by other universities, focusing on users ([University of Wisconsin Madison results][uw-survey]), and contributors ([University of California results][uc-survey]).
This may require applying for a small grant to pay students to carry out the analysis.

Collaborate with the Library for the [Open Science awards][osci-award] open-source component.

Open a digital forum for the UCL community ask questions and provide answers about open source topics. This will first start as an email forum, but it may develop into something else as the community grows.

#### Year 2-3

Data scrapping and metrics analysis will be improved to measure citations on publications, risk of software dependencies and licensing.
Additionally, the same analysis will be done on closed software developed within UCL. This will highlight risks and needs of that closed source software while encourage inner source[^innersource] practices within UCL.
This will require access to organisations and repositories we may not have at the moment and stakeholders will need to promote the need.
This is also an important security exercise and we expect ISD's Information Security Group to be involved.

Develop and publish guidance on how to release open source outcomes (software, hardware, data, or educational resources) withing UCL. 
Including licenses, development models, community engagement, and commercial opportunities.
This will need to involve the Library, ARC, Computer Science, Arena, ISD DigiEd, Innovation & Enterprise, UCLB, UCLC and Institute of Making.

Once those guides are developed, ARC Education will develop and deliver short courses covering them in a practical manner. 
Those courses will be available to all the university through Organisational Development for post-graduate students and staff, and through the Extended Learning Opportunities Programme for undergraduate students. 

Promote existing and develop new opportunities for students to collaborate with open source communities through out their degree. 
We are aware of Computer Science modules and master programmes[^csprogs]. 
Through those opportunities, students will be also interacting with various industries that are also open source users and contributors.
Though this may start with Computer Science students, it won't only be focused on STEM disciplines, but aimed to all programs.

Collaborate with already established international open source hackathons such asUN Hackathon and/or NASA Open Science.


#### Year 3-5

Continue with the metrics analysis adding new parameters and properties that help us to get a better picture. Developing therefore a recommendation on where the university should invest money or efforts based on the estimated risks of the projects and their dependencies.

Continue supporting and delivering open source training programmes.

Launch a mentoring programme for people with larger experience in open source to help others to implement practices to nurture the community around their open source product.

Develop guidance about Commercial Open Source Software (COSS), collaborating with the Library, Centre for Digital Innovation (CDI), the School of management, Innovation & Enterprise, and UCLB.
This should cover licensing possibilities as well as business models.

<!-- footnotes -->
[^innersource]: Inner source is the use of open source software development best practices and culture within an organisation during the development of closed source software.
[^csprogs]: Artificial Intelligence and Data engineering and Software Engineering master programmes are two programs which in collaboration with ARC will include group projects with open source communities on 2026-2027.
<!-- TODO: ASK alex for module he's doing app for -->
<!-- end footnotes -->

<!-- links -->
[ccmi]: https://ccmi-cdt.org/
[curioss]: https://curioss.org/
[chaoss]: https://chaoss.community/
[hpsf]: https://hpsf.io
[uw-survey]: https://uw-madison-dsi.github.io/open_source_survey_results/
[uc-survey]: https://www.youtube.com/watch?v=fFoLmb6o7Z8
[uc-survey-abs]: https://web.archive.org/web/20250905052446/https://2025.fossy.us/schedule/presentation/334/
[osci-award]: https://www.ucl.ac.uk/library/open-science-research-support/open-science/about-office-open-science-scholarship/ucl-open-science
<!-- end links -->


*project scope*
> all the tasks and deliverables that will be executed in your project to reach your business objectives

*project schedule*
> a timeline for the project by estimating how long it will take to get each task completed. Gantt chart

*Marketing Strategy*
> distribution channels, pricing, target customers, among other aspects of your marketing plan or strategy.


#### Resources
*project budget*
> Your budget is an estimate of everything in your project plan and what it will cost to complete the project over the scheduled time allotted. Personnel costs, software or hardware costs, consulting fees, training costs and contingency funds

*Financial Appraisal*
> explain how the financial benefits outweigh the project costs.


### Organisation

*Project Governance*
> ll the project management rules and procedures that apply to your project. For example, it defines the roles and responsibilities of the project team members and the framework for decision-making.

The UCL OSPO will comprise a core team from ARC and _at least one_ delegated representative from each team or department in the university that has a stake in open source.

These teams are:
- The Department of Computer Science;
- The Sainsbury Wellcome Centre's Neuroinformatics Unit;
- The Office of Open Science and Scholarship;
- ISD;
- Digital education;
- The Bartlett Centre for Advanced Spatial Analysis;
- and Mechanical Engineering.

The emphasis is on _at least_, because we aim to encourage members from these and other teams to join voluntarily.

Governance to use UCL's structure digital research board (ARC) or the one from Library.

Roles:

working groups


*Communication Plan*
> The communication plan can help foster an atmosphere of transparency and engagement among stakeholders. The plan outlines how, when and what will be communicated so that everyone is informed and has a shared understanding.
*Progress Reports*

### Supporters

## How will we know if this worked out?
*Success Criteria*

## References

- https://www.cni.org/topics/ci/guide-to-set-up-university-open-source-programs-office-ospo
- https://research.redhat.com/blog/article/building-a-university-ospo-bolstering-academic-research-through-open-source/
- https://opensource.com/article/20/10/rit-ospo
- https://opensource.utexas.edu/participation-pathway

# Checklist
- [ ] project’s objectives, 
- [ ] costs and 
- [ ] benefits
- [ ] financial appraisal,
- [ ] proposal,
- [ ] strategy and 
- [ ] marketing plan 
- [ ] offers a full look at how the project will benefit the organization
- [ ] if a project business case is not anchored to reality, and doesn’t address a need that aligns with the larger business objectives of the organization, then it is irrelevant.
- [ ] why, what, how and who of your project.
- [ ] Business problem - aligned with business goals
  - [ ] What's solving? what's the opportunity?
  - [ ]  “Lead with the need.” Your first job is to figure out what that problem or opportunity is, describe it, find out where it comes from and then address the time frame needed to deal with it.
- [ ]  Identify the Alternative Solutions
  - [ ] How do you know whether the project you’re undertaking is the best possible solution to the problem defined above? 
	1. Note the alternative solutions.
	1. For each solution, quantify its benefits.
	1. forecast the costs involved in each solution.
	1. Then figure out its [feasibility](https://www.projectmanager.com/training/how-to-conduct-a-feasibility-study).
	1. Discern the risks and issues associated with each solution.
	1. Finally, document all this in your business case.
- [ ] Recommend a Preferred Solution
  - [ ] a decision matrix to help you prioritize the solutions to best choose the right one.
- [ ] Describe the Implementation Approach
- [ ] Components
  - [ ] Executive summary
  - [ ] Project Definition
  - [ ] Vision, Goals and Objectives (You’ll need to define your project vision, goals and objectives.)
  - [ ] Project Scope
  - [ ] Background Information
  - [ ] Success Criteria and Stakeholder Requirements
  - [ ] Project Plan
  - [ ] Project Budget
  Your budget is an estimate of everything in your project plan and what it will cost to complete the project over the scheduled time allotted. 
  - [ ] Project Schedule (Gantt)
  - [ ] Project Governance 
  - [ ] Communication Plan
  - [ ] Progress Reports 
  - [ ] Financial Appraisal
  - [ ] Market Assessment
  - [ ] Competitor Analysis
  - [ ] SWOT Analysis - identify your organization’s strengths, weaknesses, opportunities and threats.
  - [ ] Marketing Strategy
  - [ ] Risk Assessment


