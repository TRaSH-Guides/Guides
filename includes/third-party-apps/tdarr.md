### Tdarr

[Tdarr](https://tdarr.io/){:target="\_blank" rel="noopener noreferrer"} is a distributed, node-based transcode-automation system that runs FFmpeg/HandBrake jobs across a central server and any number of worker nodes, driven by a conditional plugin-stack rule engine per library.

- Architecture: `Tdarr_Server` (central) plus any number of `Tdarr_Node` workers, runnable on separate machines (Windows, Linux including arm/arm64, and macOS) to put spare hardware to use. Worker types are independently scalable: Transcode-CPU, Transcode-GPU, Health-Check-CPU, Health-Check-GPU.
- Plugins are JavaScript, sourced from the public [Tdarr_Plugins](https://github.com/HaveAGitGat/Tdarr_Plugins){:target="\_blank" rel="noopener noreferrer"} repo or an in-app plugin creator, chained into Filters (codec, resolution, size, age) gating Actions (transcode, remux, standardize/strip audio and subtitle streams) — a step only fires if its filter matches.
- Distinctive beyond "it transcodes": video health/corruption checking as its own first-class worker type, not a plugin bolt-on, plus a scheduler, folder watcher, worker-stall detection, and load balancing across libraries.
- Nvidia GPU transcoding is explicitly documented (including an unRAID plugin path); check current plugin support before assuming QSV/AMD acceleration.
