# Contributing

👋 Thanks for your interest in our website and open source at UCL!

If you're from UCL and want to get involved in our open-source work, please feel encouraged to [email us], or contact the ARC collaborations team via [MyServices].

If you've spotted a bug, or want to contribute to **these website pages**, please either [open an issue] or [fork] and open a [pull request]!

> [!NOTE]
> Some of the issues in this repository are action items for us in our open-source efforts and not necessarily related to this website.

## Build the site locally

You can build and test your changes locally with the [official Jekyll Docker image](https://hub.docker.com/r/jekyll/jekyll):

```sh
curl -O https://raw.githubusercontent.com/actions/jekyll-build-pages/refs/heads/main/Gemfile
docker run --rm --volume="$PWD:/srv/jekyll" --volume="$PWD/vendor/bundle:/usr/local/bundle" -p 4000:4000 -it jekyll/jekyll:latest jekyll serve
```
or 
```sh
curl -O https://raw.githubusercontent.com/actions/jekyll-build-pages/refs/heads/main/Gemfile
docker run --rm --volume="$PWD:/srv/jekyll" --volume="$PWD/vendor/bundle:/usr/local/bundle" -p 4000:4000 -it jekyll/jekyll:latest jekyll serve
```

It's also possible to build (or serve) the site locally with Jekyll through `bundle`, but you'll need the Gemfile from GitHub:

```sh
wget https://raw.githubusercontent.com/actions/jekyll-build-pages/refs/heads/main/Gemfile
bundle install
bundle exec jekyll build
# or bundle exec jekyll serve
```

## Pull-request artifact

When you [submit a pull request](https://github.com/UCL/open-source/pulls), a GitHub Action workflow will build the website and upload a `Preview` artifact that you can download, unzip and then inspect locally with

```sh
unzip Preview.zip
python3 -m http.server
```

You can then access the preview at `http://127.0.0.1:8000/open-source/`.
You're encouraged to open a draft pull request while you're developing.
This will still trigger a build.

## Running the linters locally

We use [`lychee`] to check for broken links and [`vale`] (with [`proselint`]) to try to keep the prose consistent (particularly as different people are contributing to our business case).
We also use [`typos`](https://github.com/crate-ci/typos) to check for… typos.
These can be installed in several ways.

macOS Homebrew users can simply:

```sh
brew install lychee vale typos-cli
```

or the first two via Linux Snap:

```sh
sudo snap install lychee vale
```

or check each tool's documentation for a different installation method.

[`lychee`] should be run over the built site output:

```sh
lychee _site
```

There is a top-level `.lycheeignore` file for anything that is a false positive.

[`vale`] and [`typos`] can run directly over the site output or directly over the markdown files:

```sh
vale sync
vale ospo/business-case.md  # for example
typos ospo/business-case.md
```

There are top-level files: `.vale.ini` and `.typos.toml` to configure each.
In particular, false-positives found by [`typos`] can be [excluded with regular expressions](https://github.com/crate-ci/typos/blob/master/docs/reference.md#example-configurations).

----

## Pull request flow

(Information for maintainers)

- Changes are made via [pull requests](https://github.com/UCL/open-source/pulls); at least one person from the open-source team with commit rights will need to be involved.
- If approved with no comments, **the approving reviewer should merge** (to keep things moving).
- If approved with comments, a requester with commit rights is generally trusted to merge once they're addressed.
  - The requester can ask for re-review if they think it's needed or if 'Changes requested'.
- Changes to the business case should have the `business case` label applied.
- Changes to the business case or substantial additions and changes to the text (new guides etc.) should seek review from as many members of the open-source team as can give their time.

----

[email us]: mailto:open.source@ucl.ac.uk
[MyServices]: https://myservices.ucl.ac.uk
[open an issue]: https://github.com/UCL/open-source/issues/new
[fork]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
[pull request]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
[Jekyll]: https://jekyllrb.com
[`lychee`]: https://lychee.cli.rs
[`vale`]: https://vale.sh/docs
[`proselint`]: https://github.com/errata-ai/proselint
