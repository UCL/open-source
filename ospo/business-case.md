---
layout: default
title: Proposed Business Case
crumbs:
  - link: /ospo/business-case
    text: "Proposed Business Case for UCL's Open Source Programme Office"
---


# UCL's Open Source Programme Office - Business Case

#### *Executive Summary*

<!--
> help them understand the project’s purpose, benefits and implications. Some components of an executive summary include the project overview, business need, proposed solution to the need, cost estimate, return on investment, risks, timeline and a call to action.
-->

Our university, as with many institutions and organisations around the globe, depends on open source,
whether that is software, hardware, data, or other resources such as research and educational outputs.
Open source software is everywhere and it has a huge economic impact.
The [State of Open Source paper][sospaper] shows that 96% of all software included open-source software components.
Moreover, a [study from the Harvard Business School][harvard-oss] has shown recently that open-source software generated $8.8 trillion of value and production costs are reduced by a factor of 3.5 if open-source software were not available.
Open source "products" apart from software haven't been analysed in such detail yet.
However, from the point of view of an university they are still very important, for example for the Open Science reproducibility mission as well as for the creation of Open Educational resources.

An Open Source Programme Office (OSPO) will coordinate the usage and development of open source, as well as nurturing its adoption across the university.
We propose three main pillars that an OSPO in UCL should cover: Research, Education and Infrastructure,
supported by three main foundations: Training, Community and Policy.
With those six aspects we are increasing collaboration and visibility (within and outside UCL), as well as providing insight into the stronger and weaker points of our ecosystem and dependencies.
This office will provide: a service to obtain metrics, deliver training, and provide mentorship and guidance on running open-source projects;
a medium to support grant applications and compliance with respect to open-source requirements;
a hub of communication between the UCL community, innovation and enterprise team and external partners;
and an advocacy platform for promoting open-source culture and practices, producing policy recommendations for the university.

To achieve this, we propose to build on what UCL's [Advanced Research Computing Centre][arc] (ARC) and [Office for Open Science and Scholarship][ooss] have created,
and add components through out the next five years.
Costs will be shared across different departments across UCL,
starting with the current 0.3 FTE provided by ARC and increasing it to a shared 3 FTE across the university at the end of this period.

Being the first UK university to have an OSPO will provide a service not available elsewhere in the country to our researchers, staff and students.
It will also bring UCL greater visibility in open source communities, attracting talented workers and students, as well as investment from external bodies.


[sospaper]: https://www.synopsys.com/software-integrity/resources/analyst-reports/open-source-security-risk-analysis.html#introMenu
[harvard-oss]: http://dx.doi.org/10.2139/ssrn.4693148
[arc]: https://www.ucl.ac.uk/arc
[ooss]: https://www.ucl.ac.uk/library/open-science-research-support/ucl-office-open-science-and-scholarship

## Context
<!--
> context for your project, explaining the problem that it's meant to solve and how it aligns with the organisation's vision and strategic plan
-->

UCL has a long history of open-source software development for research and open-source educational resources.
In a recent study, we identified more than a thousand open-source software projects owned[^owned] by the UCL community on the GitHub platform that are directly related to UCL research, publications, or teaching.
The oldest[^oldest] of these projects dates back to 1997, a decade before the GitHub platform was created, and is still one of our most active projects today.

We know that UCL has given birth to open source communities such as the [Open Street Map][osm][^osmap-ucl], which was supported and hosted by UCL from 2004 when it was created, to at least 2008.
This platform provides open-source-licensed map data to everyone, free to use, edit and distribute.
It is used by many mapping applications, transport companies, government agencies, humanitarian organisations, news sites and websites[^osm-companies].
A more recent example is the [BrainGlobe Initiative][bgi] that was established by researchers at the Sainsbury Wellcome Centre and the Technical University of Munich in 2020.
They have developed a whole ecosystem of research software tools, and nurture a community of researchers that was, last year, recognised by receiving an international award for its contribution to open, accessible and collaborative neuroscience[^bgi-award]. 

Those are only three examples of many we could quote, and we are sure that there are many others that we don't know within UCL.
As researchers have become more familiar with the benefits of open-source development, and funding bodies around the world have started to request that software created with public money is openly released, we have seen an increase in researchers seeking to follow open-source practices.

Open source projects enable collaboration and discoverability.
However, open-source projects often also suffer from a lack of support and rely heavily on volunteer effort.
As an organisation that uses and produces open source, we should be more aware of our production and dependencies, and how to support them better.
This is the main objective of the Open Source Programme Office we propose.
Mapping and cataloguing all the open source we use and generate, as well as what we depend on, helps us to have an overview of where the needs are within our community, and therefore act on them. <!-- Through training, guidance, collaborating, lobbing,  -->

This problem is commonly represented by [the Dependency xkcd.com webcomic by Randall Munroe][xkcd-dep] (shown below), which represents the fragility of modern digital infrastructure.

{% include figure.html
   path="https://imgs.xkcd.com/comics/dependency_2x.png"
   overtitle="Dependency"
   alt="XKCD comic strip showing a structure formed by blocks one on top of each other. The text on top says ''All modern digital infrastructure''. In the bottom right there's a small block that gives support to the whole structure above, labelled ''A project some random person in Nebraska has been thanklessly maintaining since 2003''"
   title="Someday ImageMagick will finally break for good and we'll have a long period of scrambling as we try to reassemble civilization from the rubble."
   fignum="1"
   caption="Dependency comic strip from xkcd.com."
   captionurl="https://xkcd.com/2347/"
   captionlicense="CC-By-NC"
   height="300px" %}


<!-- UCL vision + strategic plan. (ARC + OOSS) -->
UCL's [Advanced Research Computing Centre (ARC)][arc] has led nationally the creation of research software engineering (and other digital research technical professional) roles within the sector.
Similarly the [Office of Open Science and Scholarship][ooss] has promoted the adoption of open practices and approaches across universities.
This puts UCL in an exceptional position to provide the support that open source needs across all parts of the university, and be at the forefront of open source within the UK.

<!-- Footnotes -->
[^owned]: Where "owned" simply denotes project ownership: open-source development work done by UCL staff in aid of UCL research or education.
[^oldest]: [STIR](https://github.com/UCL/STIR) - The Software for Tomographic Image Reconstruction.
[^osmap-ucl]: [Open Street Map][osm] is a crowdsourced mapping platform initiated in [2004 at UCL][osmapref] by Steve Coast at the Bartlett Centre for Advanced Spatial Analysis (CASA).
[^osm-companies]: [Open Street Map list of prominent users][osmap-users] lists also some universities, but unfortunately not UCL.
[^bgi-award]: The 2025 International Prize by the Neuro-Irv and Helga Cooper Foundation Open Science Prizes Selection Committee is organised by The Tanenbaum Open Science Institute. More information is available in the [Sainbury Wellcome Centre press release][swc-pr].
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

Though the goals of organisations across these domains differ when establishing an OSPO, they create a fabric that helps those organisations to collaborate and combine efforts to maximise the impact (and support) of open-source products. Some activities that an OSPO may do are:

- to advocate for open source practises within an organisation through community engagement;
- to measure usage of and dependency on open (and closed!) source projects;
- to measure the organisation's impact on open source;
- to mitigate associate risks (unlicensed code, vendor lock-in, licensing misuse, etc);
- to promote, guide and educate internal and external community members on open source culture from technical, social, political and economic perspectives;
- to push policy forward that safeguards open source and protects the technological sovereignty[^sovereignty] of the institution.

Those activities refer to all areas of the organisation, whether research, teaching or their business side, while promoting internal collaboration between departments and external collaboration across institutions.

{% include figure.html
   path="./Activities-of-academic-OSPO.png"
   alt="A set of circles with arrows pointing to a central larger circle with the acronym OSPO written in the Centre. Each of the small circles contain a small icon related with the activity they refer to and coloured differently of the rest. There's also a text description for each circle, and they say: Developing and sharing best practices; Educational efforts; Working with Tech Transfer and External Partners; Tools and infrastructure to support OSS; Community Building; Supporting the creation of new OSS by the academic community; Advocacy and Policy; and, Funding and financial support."
   fignum="2"
   caption="Common activities managed by an academic OSPO. From <a href='https://doi.org/10.5281/zenodo.13910682'>Young, et al. (2024)</a>."
   captionlicense="CC-By"
   height="300px" %}

These activities, however, are not new to OSPOs. Over the years, different groups within organisations have been engaging in some of them. For example, Oxford University had a group named [OSS Watch][oss-watch] between 2003-2014 that provided unbiased advice and guidance on the use, development, and licensing of free software, open-source software, and open-source hardware. Similarly, the [Software Sustainability Institute][ssi] has been advocating for better software practices in research across the UK since 2010.

A more detailed definition of an academic OSPO can be found in [Young, et al. (2024)][young-2024].

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

Open Source is a fundamental component of our research and university infrastructure. However, this is usually forgotten or not even considered. We do not know how much we depend on it. Equally, we know very little about the social, research, and economic impact that the open-source code generated by UCL has. Contributing to open-source projects requires more than technical knowledge, it is tied to social and economic aspects, and an OSPO helps to make it more accessible. An OSPO in UCL will benefit the following areas.

- Research
  - Provide guidance on sustainability, community engagement and licensing to increase reuse and impact of UCL's software.
- Education
  - Train students and staff on the use of and contribution to open-source projects.
  - Promote open-source alternatives to tools taught and used in modules, allowing students to continue practising the learnt skills when losing access to licensed tools once left UCL.
- Digital infrastructure
  - Reveal the extent to which business-critical systems such as Moodle, Portico, HR and financial management, and departmental administration are dependent on open source.
  - Provide support for the use of open-source tooling, reducing procurement costs.
  - Enable cross-department collaboration on locally developed solutions.
- Community
  - Facilitate collaboration with other institutions for similar tasks.
- Policy
  - Include open-source solutions and digital sovereignty into UCL procurement decisions.
- Measuring and enhancing impact
  - Collate metrics on what is created within/with help from UCL, and what we depend on.
  - Use data to attract further funding and collaborations.
  - Promote development of skills that will help students gain employment. Mentorship, coaching and collaborations are skills that will be gained as part of successful open-source projects.
  - Attract talent from open source communities.
  - Reduce vendor lock-in risks.

[^sovereignty]: The term technological or digital sovereignty refers to an institution being able to exercise control over its technology infrastructure. It is also referred as digital idependence of vendor lock-in. This is an increasing challenge with the growth of Artificial Intelligence solutions; factors such as where the data used to generate the models is stored (data residency), as well as the models themselves, who operates and controls the technology, and how the data are accessed, can all lead to a lack of control and complex risk landscape.


### Risks of not having an OSPO

One of the biggest difficulties in large institutions is communication. This is aggravated when there is no central hub.
In the case of open source, members of our community are mostly self-guided, having to rediscover everything from scratch.
Not having one central hub of training and information on these topics means our community keeps reinventing rather than collaborating.

Publicly available and licensed reusable material is increasingly understood as a research output, and expected as project deliverables by funding bodies and excellence frameworks.
Without an OSPO researchers lack guidance on producing these outputs in a way that supports their long-term sustainability.

A major risk that an OSPO mitigates is a legal one.
One of the mandates of an OSPO is to develop an informed organisation-wide strategy for licensing open-source projects and to provide guidance to developers and maintainers.
In our recent study, we noted 36.1% of UCL's open-source projects are unlicensed, meaning legally unusable by anyone.
We also detected some projects violating the licencing rules of their dependencies. This could ultimately result in lawsuits and incur significant costs and reputational damage.

Finally, there are also financial risks.
Without an OSPO, the university may spend on closed source products when there are good and cheaper open-source alternatives.
This can result in vendor lock-in, leading to an inability to pivot away from expensive contracts (at least without significant costs),
or being locked-out in case of geopolitical circumstances[^icc-case].
Choosing open-source solutions without robust guidance can lead to expensive failures or support costs.
Conversely, with an OSPO open source metrics are included within the procurement process and support is available for teams to develop the skills to maintain software we depend on.
This not only puts UCL in a better position, but it also contributes to improvements for users around the world and to the growth and reputation of the internal team.

<!-- footnotes -->
[^icc-case]: [Microsoft suspend access to email account to an International Criminal Court prosecutor][ms-icc] is a very recent case of situations that could arise when running most of our infrastructures on foreign companies.
<!-- end footnotes -->

<!-- links -->
[ms-icc]: https://www.nytimes.com/2025/06/20/technology/us-tech-europe-microsoft-trump-icc.html
<!-- endlinks -->

## How would it work at UCL?

An OSPO in UCL will become a team providing a central hub of communication, research, training and support, with different scopes. 
The team will be composed by a pool of staff and students from across the university, and managed by a committee formed by delegates representing different aspects of the university (research, education, infrastructure, community, policy, and professional services).
This support is expected to be provided in-kind by different departments (0.2-0.4FTE each). However, for certain projects and activities OSPO members will look for funding sources to accomplish them.

### Plan

<!--
*project definition*
> provide general information about your projects, such as the business objectives that will be achieved and the project plan outline. It offers a comprehensive overview of the project including its objectives and scope. Here, include details such as the objectives, stakeholders, scope, expected outcomes and constraints.

*project plan*
> Figure out the tasks you’ll have to take to get the project done. Estimate how long it will take to complete each one.

*risk assessment*
> identify and analyse the risks associated with your project activities. From there, you can assess the likelihood and impact of each and rank them based on this information. The risk assessment makes it easier to focus on the most pressing risks and includes a mitigation strategy to reduce the impact in case the risk comes to fruition.
-->

#### Continue work

Through the [past years][reports], members of the proposed OSPO have been already providing some community support as set out below. This is expected to continue.
For example, we will continue helping to organise and advertise Summer of Code programmes such as [Google's, where some members of UCL have been participating][ucl-gsoc] over years, throughout the student community.
The OSPO will maintain the support to the already existing communities that are related with open source across campus, such as [Linux User Group][lug], [Latex User Group][Latug], [Python Community of Practice][PCoC], [R User Group][Rusers], and various code clubs and student societies. 

We are working with funding bodies and external stakeholders to promote open source, such as UKRI, DiRAC, Software Sustainability Institute. Activities include helping to draft future policy and funding calls.

The OSPO will continue to strengthen ties with international open source networks we are members of, such as the Community for University and Research Institution OSPOs ([CURIOSS][curioss]), the Community Health Analytics in Open Source Software ([CHAOSS][chaoss]) and the [High Performance Software Foundation][hpsf], as well as supporting other UK universities that want to develop an OSPO.

#### Year 1

During the first year the OSPO will continue to maintain and augment the metrics analysis we started last year, seeking to identify and measure all the open-source software projects arising from UCL.
Additionally, we will start to measure external projects the UCL community contributes to.
Impact reports will be published every six months from the data extracted.

The OSPO committee will be formed from UCL staff who have already engaged with us, and part of their commitment will be to define the membership terms and structure of this committee.
Additionally, the committee will start looking at details of UCL finance aspects that OSPO activities could have more impact and propose projects to implement them,
and evaluate the feasibility to endorse [UN Open Source Principles][un-principles].

In collaboration with ARC's education team, the OSPO team will map and advertise which programmes, training and resources exist in the university related to open source.
For example, the ARC-led [Centre for Doctoral Training in Collaborative Computational Modelling at the Interface][ccmi] has a strong emphasis on learning to contribute to open source communities.

We will design, distribute and analyse a survey to understand the open source needs across the UCL community. 
The design will be based on surveys run by other universities, focusing on users ([University of Wisconsin Madison results][uw-survey]), and contributors ([University of California results][uc-survey]).
This may require applying for a small grant to pay students to carry out the analysis.

The OSPO will collaborate with the UCL Libraries for the [Open Science awards][osci-award] open-source component.

Open a digital forum for the UCL community ask questions and provide answers about open source topics. <!-- This will first start as an email forum, but it may develop into something else as the community grows. / No need to define this for now. -->

#### Year 2-3

Data collection and metrics analysis will be improved to measure citations of software in publications, and risks associated with software dependencies and licensing.
Additionally, the same analysis will be done on closed software developed within UCL.
This will highlight risks and needs of that closed source software while encouraging inner source[^innersource] practices within UCL.
This will require access to organisations and repositories we may not have at the moment and stakeholders will need to promote the need.
This is also an important security exercise and we expect ISD's Information Security Group to be involved.

Guidance will be published on how to release open source outcomes (software, hardware, data, or educational resources) within UCL. 
This will cover licenses, development models, community engagement, and commercial opportunities,
and hence involve stakeholders such as the Libraries, ARC, Computer Science, Arena, ISD, Innovation & Enterprise, UCLB, UCLC and the Institute of Making.

Once those guides are developed, ARC Education will develop and deliver short courses covering them in a practical manner. 
Those courses will be available to all the university through Organisational Development for post-graduate students and staff, and through the Extended Learning Opportunities Programme for undergraduate students. 

The OPSO will promote existing and develop new opportunities for students to collaborate with open source communities throughout their degree.
Through those opportunities, students will be interacting with various industries that are open source users and contributors.
We are already aware of relevant Computer Science modules and master programmes[^csprogs],
and will build from this to cover all programmes where students develop software or hardware, not just STEM disciplines.

Collaborations will be formed with established international open source hackathons such as UN Hackathon or NASA Open Science.


#### Year 3-5

Continue with the metrics analysis adding new parameters and properties that help us to get a better picture. Developing therefore a recommendation on where the university should invest money or efforts based on the estimated risks of the projects and their dependencies.

Continue supporting and delivering open source training programmes.

Launch a mentoring programme for people with larger experience in open source to help others to implement practices to nurture the community around their open-source product.

Develop guidance about Commercial Open-Source Software (COSS), collaborating with the Library, Centre for Digital Innovation (CDI), the School of management, Innovation & Enterprise, and UCLB.
This should cover licensing possibilities as well as business models.

<!-- footnotes -->
[^innersource]: Inner source is the use of open-source software development best practices and culture within an organisation during the development of closed source software.
[^csprogs]: Artificial Intelligence and Data engineering and Software Engineering master programmes are two programs which in collaboration with ARC will include group projects with open source communities on 2026-2027.
<!-- TODO: ASK alex for module he's doing app for -->
<!-- end footnotes -->

<!-- links -->
[reports]: ./documents.html#yearly-reports
[lug]: https://github-pages.ucl.ac.uk/linux/
[Latug]: https://teams.microsoft.com/l/team/19%3A4669171c71b74d9ea23c30f7e3b9195a%40thread.skype/conversations?groupId=2435df9e-6f6e-4f1e-8f4c-e048dcabb2b8&tenantId=1faf88fe-a998-4c5b-93c9-210a11d9a5c2
[PCoC]: https://teams.microsoft.com/l/team/19%3A85c78bc816764ae5982ae7b4997b2f47%40thread.skype/conversations?groupId=a3786c11-7532-44a2-a8eb-547382638405&tenantId=1faf88fe-a998-4c5b-93c9-210a11d9a5c2
[Rusers]: https://www.ellenwebborn.com/rusergroup/
[ccmi]: https://ccmi-cdt.org/
[curioss]: https://curioss.org/
[chaoss]: https://chaoss.community/
[hpsf]: https://hpsf.io
[uw-survey]: https://uw-madison-dsi.github.io/open_source_survey_results/
[uc-survey]: https://www.youtube.com/watch?v=fFoLmb6o7Z8
[uc-survey-abs]: https://web.archive.org/web/20250905052446/https://2025.fossy.us/schedule/presentation/334/
[osci-award]: https://www.ucl.ac.uk/library/open-science-research-support/open-science/about-office-open-science-scholarship/ucl-open-science
[un-principles]: https://unite.un.org/en/news/sixteen-organizations-endorse-un-open-source-principles
[ucl-gsoc]: https://blogs.ucl.ac.uk/research-software-development/arc-%E2%9D%A4-google-summer-of-code/
<!-- end links -->

<!--
*project scope*
> all the tasks and deliverables that will be executed in your project to reach your business objectives

*project schedule*
> a timeline for the project by estimating how long it will take to get each task completed. Gantt chart

*Marketing Strategy*
> distribution channels, pricing, target customers, among other aspects of your marketing plan or strategy.
-->

#### Resources

##### OSPOs Budget

<!--
 > Your budget is an estimate of everything in your project plan and what it will cost to complete the project over the scheduled time allotted. Personnel costs, software or hardware costs, consulting fees, training costs and contingency funds
-->

At the moment we have been developing the office with 0.3 FTE provided by ARC.
We estimate that for year 1 we will required a combined effort of 1 FTE,
and aim to increase that to reach 3 FTE by year 5.

We believe this could be done by contributions from other departments with a maximum of 1 FTE from ARC[^pending].

Additionally, there will be costs required for participation in conferences. Those costs could be covered by the department of the delegate.

The OSPO members will look out for funding opportunities that could buy out time from UCL staff or pay for students to carry out some of the proposed tasks.

#### Financial Appraisal

<!--
 > explain how the financial benefits outweigh the project costs.
-->

With our current information we can't provide a detailed cost analysis.
However,  we expect on year 1 that the  OSPO committee will have a better visibility on UCL expenditure to investigate and propose procurement, training and recruitment actions and practices that will benefit the sustainability of the OSPO throughout the years.
Therefore, being able to quantify what cost savings to UCL are accomplished through the OSPO activities.
For now, we believe that the main work proposed can be carried out by refocusing existing core-funded staff to work together via a single team.
Whereas, some OSPO activities will require additional funding to cover those extra efforts (FTE) needed.

Nevertheless,
UCL would be the first UK university to have an OSPO, this provides a leading position that will help
- to attract talent from open source communities,
- through providing open source training, our students will gain employability opportunities and our staff will grow their skills,
- to save licensing costs by using open-source alternatives rather than closed source software,
- to avoid time spent reinventing software or falling into licensing incompatibilities,
- to recommend where the university should invest efforts to support sustainability of projects,

### Organisation

#### Project Governance

<!--
 > ll the project management rules and procedures that apply to your project. For example, it defines the roles and responsibilities of the project team members and the framework for decision-making.
-->

The UCL OSPO will comprise a core team from ARC and _at least one_ delegated representative from each team or department in the university that has a stake in open source.

These teams include:
- The Department of Computer Science;
- The Sainsbury Wellcome Centre's Neuroinformatics Unit;
- The Office of Open Science and Scholarship;
- ISD;
- Digital Education;
- The Bartlett Centre for Advanced Spatial Analysis;
- and Mechanical Engineering.

The emphasis is on _at least_, because we aim to encourage members from these and other teams to join voluntarily.
Additionally, we would like participation from Innovation & Enterprise and UCLB to collaborate on the guidance provided about the commercialisation of open-source products.

This committee will report to UCL's [Digital Research Board][drb] and the Open Science & Scholarship Committee.
<!-- Does OSSC has a website? -->

#### Communication Plan

<!--
 > The communication plan can help foster an atmosphere of transparency and engagement among stakeholders. The plan outlines how, when and what will be communicated so that everyone is informed and has a shared understanding.
-->

The OSPO will follow "Open Development" practices, publishing everything on its website with all the decisions and minutes publicly available.
At the moment this is available on the [wiki of this repository][wiki].

#### Progress Reports

[Yearly reports on activities and outcomes][reports] are and will be published on the website.
Metrics results will be published every six months on the website.

<!-- footnotes -->
[^pending]: ARC maximum contribution is subject to ARC Senior Leadership Team approval.
<!-- end footnotes -->
<!-- links -->
[wiki]: https://github.com/UCL/open-source/wiki
[drb]: https://www.ucl.ac.uk/advanced-research-computing/digital-research-and-innovation-board-terms-reference
<!-- end links -->

### Supporters

ARC supports this initiative, providing at the moment 0.3 FTE and funding the 4-week deployment of the open source metrics tool last year.

<!-- Can any provide FTEs or financial support? -->
The Neuroinformatics Unit at the Sainsbury Welcome Centre supports the OSPO and has developed an open source summer school aligned with the OSPO objectives.

ISD ...

CASA ...


## How will we know if this worked out?

The OSPO will start with the following success criteria:

- Whether the UCL community feels that the OSPO has supported them.
  We will record engagement with and feedback on our efforts, such as people trained, advice given and projects supported.
- Whether the OSPO's activities have engaged every part of UCL, supporting all faculties, departments and centres.
- Better tracking of UCL-produced open-source software will allow us to assess whether its use externally and impact have increased.
- Whether OSPO sustainability is been demonstrated.
- Longer term, quantifiable financial impacts will be tracked, such as the replacement of closed-source products with open alternatives leading to lower procurement and licensing costs.
- Our activities attracts external funding and opportunities.

## Mision, vision and goals

Starting point for the committee that will be formed and vote on them:

**Mission Statement**

<!-- What and How; Doing now towards goals
  > You’ll need to define your project vision, goals and objectives.
-->

To support and train the UCL community to reinforce involvement and collaboration with open source communities, increasing our research impact and students' employability, strengthening industry links, and reducing costs.

**Vision**
<!-- Why | meaning; Building towards the future -->

To establish UCL as a university that nurtures open source development, supporting students and staff in their open source needs.

**Goals**

- Identify projects that need support (internal and external);
- Train UCL members on open source technically and culturally;
- Promote open-source infrastructure;
- Study impact of open source within the university;
- Collaborate with external communities and industry;
- Provide legal guidance on licensing and open source contributions.

<!-- **objectives** -->

<!-- what would be the difference between objectvies here and the one set under § Plan? -->


<!--
> *explain how it fits a niche or serves a need*
-->


## References

- [University champions open source with new OSPO][rit-opensource] - Stephen Jacobs & Scott Bureau (2020)
- [Guide To Set Up University Open Source Programs Office (OSPO)][cni-guide] - Sayeed Choudhury (2022)
- [Mandate for the CERN Open Source Program Office (OSPO)][cern-mandate] - CERN (2023)
- [Building a university OSPO: Bolstering academic research through open source][ucsc-redhat] - Stephanie Lieggi (2024)
- [A Definition of an Academic OSPO][young-2024] - Jeffrey Young et al. (2024)
- [The Value of Open Source Software][harvard-oss] - Manuel Hoffmann, Frank Nagle and Yanuo Zhou (2024)
- [2025 Open Source Security and Risk Analysis][sospaper] - BlackDuck (2025)

<!-- extra links  -->
[cni-guide]: https://www.cni.org/topics/ci/guide-to-set-up-university-open-source-programs-office-ospo
[ucsc-redhat]: https://research.redhat.com/blog/article/building-a-university-ospo-bolstering-academic-research-through-open-source/
[rit-opensource]: https://opensource.com/article/20/10/rit-ospo
[utexas-participation]: https://opensource.utexas.edu/participation-pathway <!-- no available! -->
[cern-mandate]: http://dx.doi.org/10.17181/CERN.AL8T.E9WW

---
