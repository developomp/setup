> **!! WARNING !!**\
> **THIS PROJECT IS STILL UNDER DEVELOPMENT**

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square">
</p>

<p align="center">
  My <a href="https://www.archlinux.org">Arch linux</a> based desktop setup
</p>

---

Purpose:

- To provide myself materials (script, guide, and other files) for cases when I need to transfer to other machine, or reinstall the OS.
- To answer questions others might have about my setup (e.g. what browser you use?)

If you have questions that are not answered in this repo, feel free to contact me via method listed in my [github profile page](https://github.com/developomp/developomp).

# FAQ

**Q:** Why don't you use more mainstream distros like Ubuntu?

**A:**

- arch is mainstream enough and has huge community behind it
- their package repository is huge and is easy to use
- has extensive wiki
- their philosophy matches that of mine (e.g. [user centrality](https://wiki.archlinux.org/title/Arch_Linux#User_centrality) and the DIY attitude)
- strikes a perfect balance between customizability and ease of use

<br/>

**Q:** Why don't you use easier arch-based distros like manjaro?

**A:** Though Manjaro is great and adds some feature arch linux does not provide out of the box (such as [mhwd](https://wiki.manjaro.org/index.php/Manjaro_Hardware_Detection)), it's too bloated for my liking.

# Hardware

| name    | model                                  |
| ------- | -------------------------------------- |
| Machine | LG 15U480-KP50ML Laptop (15U480-KA5MK) |
| CPU     | intel i5-8250U                         |
| GPU     | Nvidia MX 150                          |

## RAM

| model                             | size |
| --------------------------------- | ---- |
| SK Hynix HMA81GS6AFR8N-UH (stock) | 8GB  |
| Samsung M471A1K43CB1-CRC (added)  | 8GB  |

## Storage

| ID\* | model                                  | Size  |
| ---- | -------------------------------------- | ----- |
| 1    | SK Hynix HFS128G39TND-N210A (30002P10) | 128GB |
| 2    | Samsung SSD 860 PRO 512GB (RVM02B6Q)   | 512GB |

\*arbitrary index I gave. Has no meaning.

## Partitioning

- unallocated space at the end are for overprovisioning
- no swap partition

more information about efi partition can be found in [this](https://wiki.archlinux.org/title/GRUB) arch wiki.

| drive id\* | format | size      | mount location   | purpose       |
| ---------- | ------ | --------- | ---------------- | ------------- |
| 1          | FAT32  | 300MiB    | /boot/efi        | EFI partition |
| 1          | ext4   | 10000MiB  | /                | root          |
| 2          | ext4   | 450000MiB | /media/pomp/data | data storage  |

\*index from [storage](#Storage)

## Peripherals

|    peripheral | model                                                                                                                                                                                                        |
| ------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|         mouse | [Logitech G402 Hyperion fury](https://www.logitechg.com/en-eu/products/gaming-mice/g402-hyperion-fury-fps-gaming-mouse.html) I got from a [giveaway event](https://blog.naver.com/yjcomicsblog/221432692995) |
|     headphone | [NOX-2](https://www.e-nox.co.kr/theme/s007/index/product_view01.php?wr_id=16)                                                                                                                                |
| laptop cooler | [ABKO NCORE NC500](http://ncore.co.kr/shop/product_item.php?ItId=2586312930)                                                                                                                                 |

# Sources

## wallpapers

### wallpaper 1

<img alt="wallpaper 1. Cozy cafe with large window" src="./wallpaper1.png" width="75%">

- [a video](https://www.youtube.com/watch?v=QEWV6fiYaDU) from [Chillhop Music](https://www.youtube.com/channel/UCOxqgCwgOqC2lMqC5PYz_Dg)
- Artwork by [Jeff Östberg](https://jeffostberg.se​)
- Animation by [Geneviève Delacroix](http://www.genevievelacroix.com)

### wallpaper 2

<img alt="wallpaper 2. An astronaut on moon looking at earth" src="./wallpaper2.png" width="75%">

- image from [wallpaperaccess](https://wallpaperaccess.com/full/2752569.png)
- the [image list](https://wallpaperaccess.com/simple-earth) I found it from

# future

1TB hard drive for backup + redundancy
