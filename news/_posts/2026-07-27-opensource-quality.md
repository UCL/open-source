---
layout: post
title: Information quality of UCL's open-source repositories
date: 2026-07-27
---

Throughout the Open Source Programme Office managed by ARC at UCL we've collected some general metrics of the open-source repositories created at UCL that we've found.
We have produced community health metrics for [980 repositories][repos] (i.e., number of contributors, respond time, etc.).
You can see an example of such metrics in UCL's [Open Source Dashboard][osdashboard] (This only shows 380 repositories within the UCL and ARC GitHub organisations).

One of the hardest metrics to obtain automatically is whether the documentation on the repositories (if any) is helpful for possible users and contributors.
The next couple of weeks, and as part of the [STEMPoint work placement][stempoint], two students: Tasmin and Gideon, will help us to obtain such information. 
With those metrics, at ARC, we will be able to find out what type of training we need to focus on regarding open-source development by researchers at the university.

Tasmin and Gideon will be focusing on the following documentation aspects during the next couple of weeks. They may create an issue (or even a pull-request) pointing what is lacking on those repositories.

- Does a README exist?
- Does that README contains a description about the project?
- Does the project include installation instructions?
  - Does those installation instructions work? (we will only test them on Python projects for now)
- Does the documentation provide some basic usage example? Is there a beginner's guide too?
- If a user needs help, does the documentation points out how to find that help?
- If someone wants to contribute, do the project explain how those contributions are expected?
  - are there any rules regarding the usage of GenAI to generate such contributions?
- Does the project specify how to be acknowledged or cited on research works that benefits from this software?
  - Does the citation include a [Digital Object Identifier][doi] (DOI) pointing to a particular paper or version of the software?
- Does the repository provide a list of changes (a.k.a. [changelog][changelog])?
- Does the project have a Code of Conduct?

Additionally, they may try to classify the projects against the [United Nations Sustainable Development Goals (SDGs)][unsdg]. In the cases where there's a clear match, those would be also reported to the repository.

Feel free to [email us](mailto:open.source@ucl.ac.uk) if you have any question, comments, or your open source project is not listed yet in our [list of repositories][repos].


[repos]: https://github.com/UCL-ARC/augur/blob/mg/mgiordano4/repos.csv
[osdashboard]: https://github-pages.ucl.ac.uk/open-source-dashboard/
[stempoint]: https://www.stempoint.org.uk/
[doi]: https://en.wikipedia.org/wiki/Digital_object_identifier
[changelog]: https://en.wikipedia.org/wiki/Changelog
[unsdg]: https://sdgs.un.org/goals
