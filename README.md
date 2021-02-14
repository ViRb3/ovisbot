<p align="center">
  <img src="https://i.imgur.com/XOxm3Zb.png" alt="drawing" width="150"/>
</p>

<h1 align="center">
  OvisBot
</h1>

<h4 align="center">Open source Discord bot for CTF teams</h4>

<br />

<p align="center">

  <a href="https://www.codefactor.io/repository/github/cybermouflons/ovisbot">
    <img src="https://www.codefactor.io/repository/github/cybermouflons/ovisbot/badge">
  </a>

  <a href="http://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg">
  </a>
  <a href="https://github.com/cybermouflons/ovisbot/issues"><img src="https://img.shields.io/github/issues/cybermouflons/ovisbot.svg"/></a>

  <a href="https://github.com/ambv/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style: Black">
  </a>  
</p>

<p align="center">
  <a href="#overview">Overview</a>
  •
  <a href="#installation">Installation</a>
  •
  <a href="http://ovisbot.readthedocs.io/en/stable/index.html">Documentation</a>
  •
  <a href="#contribution">Contribution</a>
  •
  <a href="#license">License</a>
</p>

# Overview

OvisBot is a modular, feature-extensive Discord bot for managing CTF teams through discord. It facilitates collaboration and organisation by providing well defined commands to create/delete/update discord category/channels in order to structure CTF problems and provide more efficient team commmunication. In addition the bot provides basic utility functions to assist the solving process of CTF challenges (encoding schemes, etc.. ). Finally, promotes competitiveness amongst team members by providing a aut-synchronised leaderboard to common cybersecurity training platforms such as <a href="https://cryptohack.org/">CryptoHack</a> and <a href="https://www.hackthebox.eu/">Hack The Box</a>,

Note that the majority of the features are provided by isolated plugins and thus they can be enabled/disabled on demand.

This is a self-hosted bot, therefore it requires to be hosted on a private server in order to be used. Further instructions to do so are provided below. It also required a running instance of MongoDB on the server but still, the docker-based installation instructions take care of that.

# Installation

Ensure your environmental variable are set correctly in `docker-compose.yml`, then run:

```
docker-compose up --build
```

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/cybermouflons/ovisbot/tags).

# Contribution

Have a feature request? Make a GitHub issue and feel free to contribute. To get started with contributing refer to [CONTRIBUTE.md](./CONTRIBUTE.md).

### Current Contributors:

- [apogiatzis](https://github.com/apogiatzis)
- [kgeorgiou](https://github.com/kgeorgiou)
- [condiom](https://github.com/condiom)
- [npitsillos](https://github.com/npitsillos)
- [Sikkis](https://github.com/Sikkis)
- [ishtar](https://github.com/xmpf)

# License

Released under the GNU GPL v3 license.
