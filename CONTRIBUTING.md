# Contributing

Thanks for your interest in our website and open source at UCL!

If you're from UCL and want to get involved in our open-source work, please feel encouraged to [email us], or contact the ARC collaborations team via [MyServices].

If you've spotted a bug, or want to contribute to **these website pages**, please either [open an issue] or [fork] and open a [pull request]!

> [!NOTE]
> Some of the issues in this repository are action items for us in our open-source efforts and not necessarily related to this website.

You can build and test your changes locally with the [official Jekyll Docker image](https://hub.docker.com/r/jekyll/jekyll):

```sh
docker run --rm --volume="$PWD:/srv/jekyll" --volume="$PWD/vendor/bundle:/usr/local/bundle" -p 4000:4000 -it jekyll/jekyll:latest jekyll serve
```

## Contributing pull requests

It's also possible to build (or serve) the site locally with Jekyll through `bundle`, but you'll need the Gemfile from GitHub:

```sh
wget https://raw.githubusercontent.com/actions/jekyll-build-pages/refs/heads/main/Gemfile
bundle install
bundle exec jekyll build
```

When you submit a pull request to the [UCL/open-source](https://github.com/UCL/open-source), a GitHub Action workflow will build the website and upload a `Preview` artifact that you can download, unzip and then inspect locally with
```
unzip Preview.zip
python3 -m http.server
```

You can then access the preview at the address http://127.0.0.1:8000/open-source/

[email us]: mailto:open.source@ucl.ac.uk
[MyServices]: https://myservices.ucl.ac.uk
[open an issue]: https://github.com/UCL/open-source/issues/new
[fork]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
[pull request]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
[Jekyll]: https://jekyllrb.com
