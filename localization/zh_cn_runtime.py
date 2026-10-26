"""Runtime localization layer for the zh-CN yt-dlp build.

This file is passed to PyInstaller as a runtime hook.  It deliberately keeps
localization outside yt-dlp's extractor code so nightly source changes never
need to merge translated identifiers, format selectors, URLs, or site logic.
"""

from __future__ import annotations

import os
import re
import sys


# BEGIN GENERATED OPTION TRANSLATIONS
OPTION_TRANSLATIONS = {
  "--abort-on-error": "如果发生错误，则中止后续视频的下载 （别名：--no-ignore-errors）",
  "--abort-on-unavailable-fragments": "如果片段不可用，则中止下载 （别名：--no-skip-unavailable-fragments）",
  "--add-headers": "指定自定义 HTTP 头及其值，以冒号“:”分隔。 您可以使用此选项多次",
  "--age-limit": "仅下载适合给定年龄的视频",
  "--alias": "为选项字符串创建别名。除非别名以“-”开头， 否则会为其添加“--”前缀。参数根据 Python 字符串格式化 迷你语言进行解析。例如 --alias get-audio,-X \"-S aext:{0},abr -x --audio-format {0}\" 会创建 选项“--get-audio”和“-X”，它接受一个参数（ARG0） 并扩展为“-S aext:ARG0,abr -x --audio-format ARG0”。 所有定义的别名都列在 --help 输出中。别名选项可以 触发更多别名；因此请小心避免定义递归选项。 作为安全措施，每个别名最多可触发 100 次。 此选项可多次使用",
  "--ap-list-mso": "列出所有支持的多系统运营商",
  "--ap-mso": "Adobe Pass 多系统运营商（电视提供商）标识符， 使用 --ap-list-mso 获取可用 MSO 列表",
  "--ap-password": "多系统运营商帐户密码。 如果省略此选项，yt-dlp 将交互式询问",
  "--ap-username": "多系统运营商帐户登录名",
  "--audio-format": "使用 -x 时音频要转换到的格式。 （当前支持：best（默认）, aac, alac, flac, m4a, mp3, opus, vorbis, wav）。 您可以使用与 --remux-video 类似的语法指定多个规则",
  "--audio-multistreams": "允许多个音频流合并到单个文件中",
  "--audio-quality": "使用 -x 转换音频时指定要使用的 ffmpeg 音频质量。 对于 VBR，插入一个介于 0（最佳）和 10（最差）之间的值， 或特定的比特率，如 128K（默认 5）",
  "--batch-file": "包含要下载的网址的文件（“-”表示标准输入）， 每行一个网址。以“#”、“;”或“]”开头的行被视为注释并被忽略",
  "--bidi-workaround": "解决缺乏双向文本支持的终端的问题。 需要 PATH 中有 bidiv 或 fribidi 可执行文件",
  "--break-match-filters": "与“--match-filters”相同，但在视频被拒绝时停止下载过程",
  "--break-on-existing": "当遇到使用 --download-archive 选项提供的存档中 存在的文件时停止下载过程",
  "--break-per-input": "更改 --max-downloads、--break-on-existing、 --break-match-filters 和 autonumber， 使其为每个输入网址重置",
  "--buffer-size": "下载缓冲区的大小，例如 1024 或 16K（默认为 1024）",
  "--cache-dir": "yt-dlp 可以在文件系统中永久存储 某些下载信息（例如客户端 ID 和签名）的位置。 默认为 ${XDG_CACHE_HOME}/yt-dlp",
  "--check-all-formats": "检查所有格式是否实际可下载",
  "--check-formats": "确保仅从实际可下载的格式中进行选择",
  "--clean-info-json": "从 infojson 中删除某些内部元数据，例如文件名（默认）",
  "--client-certificate": "PEM 格式的客户端证书文件路径。可能包含私钥",
  "--client-certificate-key": "客户端证书私钥文件的路径",
  "--client-certificate-password": "客户端证书私钥的密码（如果已加密）。 如果未提供且密钥已加密，yt-dlp 将交互式询问",
  "--color": "是否在输出中发出颜色代码， 可选择性地以“流”（stdout 或 stderr）为前缀 以应用设置。可以是“always”、“auto”（默认）、 “never”或“no_color”（使用非颜色终端序列）。 使用“auto-tty”或“no_color-tty”仅基于终端支持来决定。 可多次使用",
  "--compat-options": "可通过恢复 yt-dlp 中做出的某些更改 来帮助保持与 youtube-dl 或 youtube-dlc 配置 兼容的选项。详情请参阅“默认行为差异”",
  "--concat-playlist": "连接播放列表中的视频。 可以是“never”、“always”或“multi_video” （默认；仅当视频构成单个节目时）。 所有视频文件必须具有相同的编解码器和流数才能连接。 “pl_video:”前缀可与“--paths”和“--output”一起使用， 以设置连接文件的输出文件名。详情请参阅“输出模板”",
  "--concurrent-fragments": "应并发下载的 dash/hlsnative 视频的片段数 （默认为 1）",
  "--config-locations": "主配置文件的位置； 可以是配置文件的路径或其所在目录 （“-”表示标准输入）。可以在其他配置文件中 多次使用",
  "--console-title": "在控制台标题栏中显示进度",
  "--continue": "恢复部分下载的文件/片段（默认）",
  "--convert-subs": "将字幕转换为另一种格式 （当前支持：ass, lrc, srt, vtt）。 使用“--convert-subs none”禁用转换（默认） （别名：--convert-subtitles）",
  "--convert-thumbnails": "将缩略图转换为另一种格式 （当前支持：jpg, png, webp）。 您可以使用与“--remux-video”类似的语法指定多个规则。 使用“--convert-thumbnails none”禁用转换（默认）",
  "--cookies": "用于读取 cookie 和转储 cookie jar 的 Netscape 格式文件",
  "--cookies-from-browser": "要从中加载 cookie 的浏览器名称。 当前支持的浏览器有：brave, chrome, chromium, edge, firefox, opera, safari, vivaldi, whale。 可选地，可以给出用于在 Linux 上解密 Chromium cookie 的 KEYRING、要从中加载 cookie 的配置文件的名称/路径， 以及（如果是 Firefox）容器名称（CONTAINER） （“none”表示无容器），并带有各自的分隔符。 默认情况下，使用最近访问的配置文件的所有容器。 当前支持的密钥环有：basictext, gnomekeyring, kwallet, kwallet5, kwallet6",
  "--date": "仅下载在此日期上传的视频。 日期可以是“YYYYMMDD”或格式为 [now|today|yesterday][-N[day|week|month|year]]。 例如，“--date today-2weeks”仅下载 两周前的同一天上传的视频",
  "--dateafter": "仅下载在此日期或之后上传的视频。 接受的日期格式与 --date 相同",
  "--datebefore": "仅下载在此日期或之前上传的视频。 接受的日期格式与 --date 相同",
  "--default-search": "对不合格的网址使用此前缀。例如， \"gvsearch2:python\" 会从谷歌视频下载两个 搜索词为“python”的视频。使用值“auto”让 yt-dlp 猜测（“auto_warning”在猜测时发出警告）。 “error”则直接抛出错误。默认值“fixup_error” 会修复损坏的网址，但如果无法修复则抛出错误而不是搜索",
  "--download-archive": "仅下载未在存档文件中列出的视频。 将所有下载的视频的 ID 记录在其中",
  "--download-sections": "仅下载与正则表达式匹配的章节。 “*”前缀表示时间范围而不是章节。 负时间戳从末尾计算。“*from-url”可用于下载 从网址提取的“start_time”和“end_time”之间的部分。 需要 ffmpeg。此选项可多次使用以下载多个部分， 例如 --download-sections \"*10:15-inf\" --download-sections \"intro\"",
  "--downloader": "要使用的外部下载器的名称或路径， （可选地）以协议（http, ftp, m3u8, dash, rstp, rtmp, mms） 为前缀以将其用于该协议。当前支持 native, aria2c, avconv, axel, curl, ffmpeg, httpie, wget。 您可以使用此选项多次为不同协议设置不同的下载器。 例如 --downloader aria2c --downloader \"dash,m3u8:native\" 将对 http/ftp 下载使用 aria2c，对 dash/m3u8 下载 使用原生下载器（别名：--external-downloader）",
  "--downloader-args": "将这些参数传递给外部下载器。 指定下载器名称和参数，以冒号“:”分隔。 对于 ffmpeg，可以使用与 --postprocessor-args 相同的语法 将参数传递到不同位置。您可以使用此选项多次 将不同的参数传递给不同的下载器（别名：--external-downloader-args）",
  "--dump-json": "安静，但为每个视频打印 JSON 信息。 除非使用 --no-simulate，否则模拟。 有关可用键的描述，请参阅“输出模板”",
  "--dump-pages": "打印使用 base64 编码的已下载页面以调试问题（非常详细）",
  "--dump-single-json": "安静，但为每个传递的 URL 或 infojson 打印 JSON 信息。 除非使用 --no-simulate，否则模拟。 如果 URL 指向播放列表，则整个播放列表信息 在一行中转储",
  "--dump-user-agent": "显示当前用户代理并退出",
  "--embed-chapters": "向视频文件添加章节标记（别名：--add-chapters）",
  "--embed-info-json": "将 infojson 作为附件嵌入到 mkv/mka 视频文件中",
  "--embed-metadata": "将元数据嵌入到视频文件中。 如果存在，还会嵌入章节/infojson，除非使用了 --no-embed-chapters/--no-embed-info-json （别名：--add-metadata）",
  "--embed-subs": "在视频中嵌入字幕（仅适用于 mp4、webm 和 mkv 视频）",
  "--embed-thumbnail": "在视频中嵌入缩略图作为封面艺术",
  "--enable-file-urls": "启用 file:// 网址。 出于安全原因，默认情况下禁用此功能",
  "--encoding": "强制指定的编码（实验性）",
  "--exec": "执行命令，可选择性地以执行时机为前缀，以“:”分隔。 “WHEN”的支持值与 --use-postprocessor 相同 （默认：after_move）。可以使用与输出模板相同的语法 将任何字段作为参数传递给命令。如果未传递任何字段， %(filepath,_filename|)q 会附加到命令的末尾。 此选项可多次使用",
  "--extract-audio": "将视频文件转换为纯音频文件 （需要 ffmpeg 和 ffprobe）",
  "--extractor-descriptions": "输出所有支持的提取器的描述并退出",
  "--ffmpeg-location": "ffmpeg 二进制文件的位置； 可以是二进制文件的路径或其所在目录",
  "--file-access-retries": "文件访问错误的重试次数（默认为 3），或“infinite”",
  "--fixup": "自动纠正文件的已知故障。 可以是 never（不执行任何操作）、warn（仅发出警告）、 detect_or_warn（默认；如果可以则修复文件，否则发出警告）、 force（即使文件已存在也尝试修复）",
  "--flat-playlist": "不提取播放列表的网址结果条目； 某些条目元数据可能缺失，并且可能绕过下载",
  "--force-ipv4": "通过 IPv4 进行所有连接",
  "--force-ipv6": "通过 IPv6 进行所有连接",
  "--force-keyframes-at-cuts": "在下载/拆分/删除部分时强制在切割处设置关键帧。 由于需要重新编码，这很慢，但生成的视频在切割处 可能具有更少的伪影",
  "--force-overwrites": "覆盖所有视频和元数据文件。此选项包括 --no-continue",
  "--force-write-archive": "强制写入下载存档条目，只要没有错误发生， 即使使用了 -s 或其他模拟选项 （别名：--force-download-archive）",
  "--format": "视频格式代码，详情请参阅“格式选择”",
  "--format-sort": "按给定字段对格式进行排序， 详情请参阅“排序格式”",
  "--format-sort-force": "强制用户指定的排序顺序优先于所有字段， 详情请参阅“排序格式”（别名：--S-force）",
  "--fragment-retries": "片段的重试次数（默认为 10），或“infinite” （DASH、hlsnative 和 ISM）",
  "--geo-verification-proxy": "使用此代理验证某些地理限制站点的 IP 地址。 实际的下载使用由 --proxy 指定的默认代理 （或者如果没有该选项，则不使用代理）",
  "--help": "打印此帮助文本并退出",
  "--hls-use-mpegts": "对 HLS 视频使用 mpegts 容器； 允许某些播放器在下载时播放视频， 并降低下载中断时文件损坏的可能性。 对于直播流，默认启用此功能",
  "--http-chunk-size": "基于块的 HTTP 下载的块大小， 例如 10485760 或 10M（默认禁用）。 可能有助于绕过网络服务器施加的带宽限制（实验性）",
  "--ignore-config": "不加载任何更多的配置文件， 除了那些通过 --config-locations 指定的。 为了向后兼容，如果在系统配置文件中找到此选项， 则不会加载用户配置。 （别名：--no-config）",
  "--ignore-errors": "忽略下载和后处理错误。 即使后处理失败，下载也会被视为成功",
  "--ignore-no-formats-error": "忽略“无视频格式”错误。即使视频实际上无法下载， 也可用于提取元数据（实验性）",
  "--impersonate": "要冒充的客户端以进行请求。例如 chrome, chrome-110, chrome:windows-10。 传递 --impersonate=\"\" 来冒充任何客户端。 请注意，强制对所有请求进行冒充可能会对 下载速度和稳定性产生不利影响",
  "--keep-fragments": "下载完成后在磁盘上保留已下载的片段",
  "--keep-video": "后处理后在磁盘上保留中间视频文件",
  "--lazy-playlist": "在接收到播放列表条目时即进行处理。 这会禁用 n_entries、--playlist-random 和 --playlist-reverse",
  "--legacy-server-connect": "显式允许与不支持 RFC 5746 安全重新协商的服务器 进行 HTTPS 连接",
  "--limit-rate": "最大下载速率（字节/秒），例如 50K 或 4.2M",
  "--list-extractors": "列出所有支持的提取器并退出",
  "--list-formats": "列出每个视频的可用格式。 除非使用 --no-simulate，否则模拟",
  "--list-impersonate-targets": "列出可冒充的可用客户端",
  "--list-subs": "列出每个视频的可用字幕。 除非使用 --no-simulate，否则模拟",
  "--list-thumbnails": "列出每个视频的可用缩略图。 除非使用 --no-simulate，否则模拟",
  "--live-from-start": "从开始处下载直播流。 目前是实验性的，仅支持 YouTube 和 Twitch",
  "--load-info-json": "包含视频信息的 JSON 文件 （使用“--write-info-json”选项创建）",
  "--mark-watched": "将视频标记为已观看（即使使用 --simulate）",
  "--match-filters": "通用视频过滤器。任何“输出模板”字段 都可以使用“格式过滤”中定义的运算符与数字或字符串 进行比较。您也可以简单地指定一个字段来匹配 该字段是否存在，使用“!field”检查字段是否不存在， 并使用“&”检查多个条件。如果需要，使用“\\”来转义 “&”或引号。如果多次使用，则只要满足至少一个条件， 过滤器就会匹配。例如 --match-filters !is_live --match-filters \"like_count>?100 & description~='(?i)\\bcats \\& dogs\\b'\" 仅匹配 非直播视频 OR 那些点赞数超过 100（或 like 字段不可用） 并且描述中包含短语“cats & dogs”（不区分大小写）的视频。 使用“--match-filters -”以交互方式询问是否下载每个视频",
  "--max-downloads": "下载 NUMBER 个文件后中止",
  "--max-filesize": "如果文件大小大于 SIZE，则中止下载， 例如 50k 或 44.6M",
  "--max-sleep-interval": "最大休眠秒数。只能与 --min-sleep-interval 一起使用",
  "--merge-output-format": "合并格式时可能使用的容器，以“/”分隔， 例如“mp4/mkv”。如果不需要合并，则忽略。 （当前支持：avi, flv, mkv, mov, mp4, webm）",
  "--min-filesize": "如果文件大小小于 SIZE，则中止下载， 例如 50k 或 44.6M",
  "--mtime": "使用 Last-modified 头来设置文件修改时间",
  "--netrc": "使用 .netrc 认证数据",
  "--netrc-cmd": "为提取器获取凭据要执行的命令",
  "--netrc-location": ".netrc 认证数据的位置； 可以是路径或其所在目录。默认为 ~/.netrc",
  "--newline": "将进度条输出为新行",
  "--no-abort-on-error": "遇到下载错误时继续下一个视频； 例如，跳过播放列表中不可用的视频（默认）",
  "--no-audio-multistreams": "每个输出文件仅下载一个音频流（默认）",
  "--no-batch-file": "不从批处理文件读取网址（默认）",
  "--no-break-match-filters": "不使用任何 --break-match-filters（默认）",
  "--no-break-on-existing": "当遇到存档中存在的文件时不停止下载过程（默认）",
  "--no-break-per-input": "--break-on-existing 和类似选项终止整个下载队列",
  "--no-cache-dir": "禁用文件系统缓存",
  "--no-check-certificates": "抑制 HTTPS 证书验证",
  "--no-check-formats": "不检查格式是否实际可下载",
  "--no-clean-info-json": "将所有字段写入 infojson",
  "--no-config-locations": "不加载任何自定义配置文件（默认）。 在配置文件中给出时，忽略当前文件中 所有先前定义的 --config-locations",
  "--no-continue": "不恢复部分下载的片段。 如果文件未分段，则重新开始下载整个文件",
  "--no-cookies": "不从文件读取/转储 cookie（默认）",
  "--no-cookies-from-browser": "不从浏览器加载 cookie（默认）",
  "--no-download-archive": "不使用存档文件（默认）",
  "--no-embed-chapters": "不添加章节标记（默认）（别名：--no-add-chapters）",
  "--no-embed-info-json": "不将 infojson 作为附件嵌入到视频文件中",
  "--no-embed-metadata": "不向文件添加元数据（默认） （别名：--no-add-metadata）",
  "--no-embed-subs": "不嵌入字幕（默认）",
  "--no-embed-thumbnail": "不嵌入缩略图（默认）",
  "--no-exec": "删除任何先前定义的 --exec",
  "--no-flat-playlist": "完全提取播放列表的视频（默认）",
  "--no-force-keyframes-at-cuts": "在切割/拆分时不强制在章节周围设置关键帧（默认）",
  "--no-force-overwrites": "不覆盖视频，但覆盖相关文件（默认）",
  "--no-format-sort-force": "某些字段优先于用户指定的排序顺序（默认）",
  "--no-hls-use-mpegts": "不对 HLS 视频使用 mpegts 容器。 不下载直播流时，此为默认值",
  "--no-ignore-no-formats-error": "当找不到可下载的视频格式时抛出错误（默认）",
  "--no-keep-fragments": "下载完成后删除已下载的片段（默认）",
  "--no-keep-video": "后处理后删除中间视频文件（默认）",
  "--no-lazy-playlist": "仅在解析整个播放列表后处理播放列表中的视频（默认）",
  "--no-live-from-start": "从当前时间下载直播流（默认）",
  "--no-mark-watched": "不将视频标记为已观看（默认）",
  "--no-match-filters": "不使用任何 --match-filters（默认）",
  "--no-mtime": "不使用 Last-modified 头来设置文件修改时间（默认）",
  "--no-overwrites": "不覆盖任何文件",
  "--no-part": "不使用 .part 文件 - 直接写入输出文件",
  "--no-playlist": "如果网址指向视频和播放列表，则仅下载视频",
  "--no-plugin-dirs": "清除要搜索的插件目录， 包括默认目录和先前通过 --plugin-dirs 提供的目录",
  "--no-post-overwrites": "不覆盖后处理的文件",
  "--no-prefer-free-formats": "不给免费容器任何特殊偏好（默认）",
  "--no-progress": "不打印进度条",
  "--no-quiet": "停用安静模式。（默认）",
  "--no-remove-chapters": "不从文件中删除任何章节（默认）",
  "--no-resize-buffer": "不自动调整缓冲区大小",
  "--no-restrict-filenames": "允许文件名中使用 Unicode 字符、“&”和空格（默认）",
  "--no-simulate": "即使使用打印/列表选项，也下载视频",
  "--no-split-chapters": "不基于章节拆分视频（默认）",
  "--no-sponsorblock": "禁用 --sponsorblock-mark、--sponsorblock-remove 和 --sponsorblock-chapter-title",
  "--no-update": "不检查更新（默认）",
  "--no-video-multistreams": "每个输出文件仅下载一个视频流（默认）",
  "--no-wait-for-video": "不等待预定的流（默认）",
  "--no-warnings": "忽略警告",
  "--no-windows-filenames": "仅最小化地清理文件名",
  "--no-write-auto-subs": "不写入自动生成的字幕（默认） （别名：--no-write-automatic-subs）",
  "--no-write-comments": "不检索视频评论，除非已知提取速度很快（别名：--no-get-comments）",
  "--no-write-description": "不写入视频描述（默认）",
  "--no-write-info-json": "不写入视频元数据（默认）",
  "--no-write-playlist-metafiles": "在使用 --write-info-json、--write-description 等时， 不写入播放列表元数据",
  "--no-write-subs": "不写入字幕文件（默认）",
  "--no-write-thumbnail": "不将缩略图图像写入磁盘（默认）",
  "--output": "输出文件名模板；详情请参阅“输出模板”",
  "--output-na-placeholder": "--output 中不可用字段的占位符（默认：“NA”）",
  "--parse-metadata": "从其他字段解析额外的元数据，如标题/艺术家； 详情请参阅“修改元数据”。“WHEN”的支持值与 --use-postprocessor 相同（默认：pre_process）",
  "--part": "使用 .part 文件而不是直接写入输出文件（默认）",
  "--password": "帐户密码。如果省略此选项， yt-dlp 将交互式询问",
  "--paths": "文件应下载到的路径。 指定文件类型和路径，以冒号“:”分隔。 支持与 --output 相同的所有类型。 此外，您还可以提供“home”（默认）和“temp”路径。 所有中间文件首先下载到临时路径， 然后在下载完成后将最终文件移动到主路径。 如果 --output 是绝对路径，则忽略此选项",
  "--playlist-items": "要下载的项目的逗号分隔的 playlist_index。 您可以使用“[起始]:[结束][:步长]”指定范围。 为了向后兼容，也支持 START-STOP。 使用负索引从右边计数，使用负 STEP 以相反顺序下载。 例如，在大小为 15 的播放列表上使用“-I 1:3,7,-5::2” 将下载索引为 1,2,3,7,11,13,15 的项目",
  "--playlist-random": "以随机顺序下载播放列表视频",
  "--plugin-dirs": "用于搜索插件的附加目录路径。 此选项可多次使用以添加多个目录。 使用“default”搜索默认插件目录（默认）",
  "--post-overwrites": "覆盖后处理的文件（默认）",
  "--postprocessor-args": "将这些参数传递给后处理器。 指定后处理器/可执行文件名称和参数，以冒号“:”分隔， 以将参数传递给指定的后处理器/可执行文件。 支持的 PP 有：Merger, ModifyChapters, SplitChapters, ExtractAudio, VideoRemuxer, VideoConvertor, Metadata, EmbedSubtitle, EmbedThumbnail, SubtitlesConvertor, ThumbnailsConvertor, FixupStretched, FixupM4a, FixupM3u8, FixupTimestamp 和 FixupDuration。 支持的可执行文件有：AtomicParsley, FFmpeg 和 FFprobe。 您还可以指定“PP+EXE:ARGS”以仅在指定后处理器 使用指定可执行文件时将参数传递给该可执行文件。 此外，对于 ffmpeg/ffprobe，可以选择在前缀后附加“_i”/“_o” 并可选地后跟一个数字，以在指定的输入/输出文件之前传递参数， 例如 --ppa \"Merger+ffmpeg_i1:-v quiet\"。 您可以使用此选项多次将不同的参数传递给不同的后处理器。 （别名：--ppa）",
  "--prefer-free-formats": "在质量相同的情况下，优先选择具有免费容器的视频格式。 与“-S ext”一起使用以严格优先选择免费容器，而不管质量如何",
  "--prefer-insecure": "使用未加密的连接来检索视频信息 （目前仅支持 YouTube）",
  "--preset-alias": "应用预定义的选项集。例如 --preset-alias mp3。 以下预设可用：mp3, aac, mp4, mkv, sleep。 更多信息请参阅末尾的“预设别名”部分。 此选项可多次使用",
  "--print": "要打印到屏幕的字段名称或输出模板， 可选择性地以打印时机为前缀，以“:”分隔。 “WHEN”的支持值与 --use-postprocessor 相同 （默认：video）。隐含 --quiet。 除非使用 --no-simulate 或 WHEN 的后期阶段，否则隐含 --simulate。 此选项可多次使用",
  "--print-to-file": "将给定的模板附加到文件。 WHEN 和 TEMPLATE 的值与 --print 相同。 FILE 使用与输出模板相同的语法。 此选项可多次使用",
  "--print-traffic": "显示发送和读取的 HTTP 流量",
  "--progress": "显示进度条，即使在安静模式下",
  "--progress-delta": "进度输出之间的时间（默认：0）",
  "--progress-template": "进度输出的模板，可选择性地以“download:”（默认）、 “download-title:”（控制台标题）、“postprocess:” 或“postprocess-title:”之一为前缀。 视频的字段可在“info”键下访问， 进度属性可在“progress”键下访问。 例如 --console-title --progress-template \"download-title:%(info.id)s-%(progress.eta)s\"",
  "--proxy": "使用指定的 HTTP/HTTPS/SOCKS 代理。 要启用 SOCKS 代理，请指定正确的方案， 例如 socks5://user:pass@127.0.0.1:1080/。 传入空字符串（--proxy \"\"）进行直接连接",
  "--quiet": "激活安静模式。如果与 --verbose 一起使用， 则将日志打印到 stderr",
  "--recode-video": "如有必要，将视频重新编码为另一种格式。 语法和支持的格式与 --remux-video 相同",
  "--remove-chapters": "删除标题与给定正则表达式匹配的章节。 语法与 --download-sections 相同。 此选项可多次使用",
  "--remux-video": "如有必要，将视频重新混流到另一个容器中 （当前支持：avi, flv, gif, mkv, mov, mp4, webm, aac, aiff, alac, flac, m4a, mka, mp3, ogg, opus, vorbis, wav）。 如果目标容器不支持视频/音频编解码器，重新混流将失败。 您可以指定多个规则；例如“aac>m4a/mov>mp4/mkv” 会将 aac 重新混流为 m4a，将 mov 重新混流为 mp4，其他所有内容重新混流为 mkv",
  "--replace-in-metadata": "使用给定的正则表达式替换元数据字段中的文本。 此选项可多次使用。“WHEN”的支持值与 --use-postprocessor 相同（默认：pre_process）",
  "--resize-buffer": "缓冲区大小从 --buffer-size 的初始值自动调整（默认）",
  "--restrict-filenames": "将文件名限制为仅 ASCII 字符， 并避免文件名中的“&”和空格",
  "--retries": "重试次数（默认为 10），或“infinite”",
  "--retry-sleep": "重试之间的休眠时间（秒）， （可选地）以重试类型（http（默认）、fragment、 file_access、extractor）为前缀以应用休眠。 EXPR 可以是数字、linear=起始[:结束[:步长=1]] 或 exp=起始[:结束[:基数=2]]。此选项可多次使用 以设置不同重试类型的休眠，例如 --retry-sleep linear=1::2 --retry-sleep fragment:exp=1:20",
  "--rm-cache-dir": "删除所有文件系统缓存文件",
  "--simulate": "不下载视频，也不向磁盘写入任何内容",
  "--skip-download": "不下载视频，但写入所有相关文件 （别名：--no-download）",
  "--skip-playlist-after-errors": "允许的失败次数，超过后跳过播放列表的其余部分",
  "--skip-unavailable-fragments": "跳过 DASH、hlsnative 和 ISM 下载中不可用的片段（默认） （别名：--no-abort-on-unavailable-fragments）",
  "--sleep-interval": "每次下载前休眠的秒数。 当与 --max-sleep-interval 一起使用时，这是最小休眠时间 （别名：--min-sleep-interval）",
  "--sleep-requests": "数据提取期间请求之间休眠的秒数",
  "--sleep-subtitles": "每次字幕下载前休眠的秒数",
  "--socket-timeout": "放弃前的等待时间，单位为秒",
  "--source-address": "要绑定的客户端 IP 地址",
  "--split-chapters": "根据内部章节将视频拆分为多个文件。 “chapter:”前缀可与“--paths”和“--output”一起使用， 以设置拆分文件的输出文件名。详情请参阅“输出模板”",
  "--sponsorblock-api": "SponsorBlock API 的网址，默认为 https://sponsor.ajay.app",
  "--sponsorblock-chapter-title": "用于 SponsorBlock 章节的标题模板。 仅在同时使用 --sponsorblock-mark 时有效。 可用键：category, start_time, end_time, percent, length, category_names。 默认为“[SponsorBlock]: %(category_names)l”",
  "--sponsorblock-mark": "在视频中标记指定的类别作为赞助部分。 根据视频的起始时间，赞助部分会变为常规章节， 并在播放器中可见。类别可以是 “all”、“default”或 SponsorBlock 类别列表 （例如“sponsor,intro”）。您可以使用 --sponsorblock-remove 或 --sponsorblock-chapter-title 更改默认行为。 详情请参阅项目页面 https://sponsor.ajay.app",
  "--sponsorblock-remove": "从视频中删除指定的类别部分。 删除的部分将不会出现在输出文件中。 类别语法与 --sponsorblock-mark 相同",
  "--sub-format": "字幕格式；接受以“/”分隔的格式偏好， 例如“srt”或“ass/srt/best”",
  "--sub-langs": "要下载的字幕语言（可以是正则表达式）或“all”， 以逗号分隔，例如 --sub-langs \"en.*,ja\" （其中“en.*”是匹配“en”后跟 0 个或多个任意字符的正则模式）。 您可以在语言代码前加上“-”以将其从请求的语言中排除， 例如 --sub-langs all,-live_chat。 使用 --list-subs 获取可用语言标签列表",
  "--throttled-rate": "假定限流并重新提取视频数据的最低下载速率 （字节/秒），例如 100K",
  "--trim-filenames": "将文件名长度（不包括扩展名）限制为指定的字符数",
  "--twofactor": "双因素认证代码",
  "--update": "将此程序更新至最新版本",
  "--update-to": "升级/降级到特定版本。 “频道”也可以是仓库。如果省略， “频道”和“标签”分别默认为“stable”和“latest”； 详情请参阅“更新”部分。支持的频道：stable, nightly, master",
  "--use-extractors": "要使用的提取器名称，以逗号分隔。 您还可以使用正则表达式、“all”、“default” 和“end”（结束网址匹配）；例如 --ies \"holodex.*,end,youtube\"。在名称前加上“-” 可以排除它，例如 --ies default,-generic。 使用 --list-extractors 获取提取器名称列表。 （别名：--ies）",
  "--use-postprocessor": "要启用的（区分大小写的）插件后处理器的名称， 以及（可选地）要传递给它的参数，以冒号“:”分隔。 ARGS 是分号“;”分隔的 NAME=VALUE 列表。 “when”参数决定后处理器的调用时间。 可以是“pre_process”（视频提取后）、 “after_filter”（视频通过过滤器后）、 “video”（--format 之后；--print/--output 之前）、 “before_dl”（每次视频下载之前）、 “post_process”（每次视频下载之后；默认）、 “after_move”（将视频文件移动到最终位置之后）、 “after_video”（下载并处理所有格式后）或 “playlist”（播放列表处理结束时）。 此选项可多次使用以添加多个后处理器",
  "--username": "使用此帐户 ID 登录",
  "--verbose": "打印各种调试信息",
  "--version": "打印程序版本并退出",
  "--video-multistreams": "允许多个视频流合并到单个文件中",
  "--video-password": "视频特定密码",
  "--wait-for-video": "等待预定的流变为可用。 传递重试之间等待的最小秒数（或范围）",
  "--windows-filenames": "强制文件名与 Windows 兼容",
  "--write-all-thumbnails": "将所有缩略图图像格式写入磁盘",
  "--write-auto-subs": "写入自动生成的字幕文件 （别名：--write-automatic-subs）",
  "--write-comments": "检索视频评论以放入 infojson。 即使没有此选项，如果已知提取速度很快，也会获取评论 （别名：--get-comments）",
  "--write-description": "将视频描述写入 .description 文件",
  "--write-desktop-link": "写入 .desktop Linux 互联网快捷方式",
  "--write-info-json": "将视频元数据写入 .info.json 文件 （这可能包含个人信息）",
  "--write-link": "写入互联网快捷方式文件，取决于当前平台 （.url, .webloc 或 .desktop）。网址可能被操作系统缓存",
  "--write-pages": "将下载的中间页面写入当前目录中的文件以调试问题",
  "--write-playlist-metafiles": "在使用 --write-info-json、--write-description 等时， 除了视频元数据外，还写入播放列表元数据（默认）",
  "--write-subs": "写入字幕文件",
  "--write-thumbnail": "将缩略图图像写入磁盘",
  "--write-url-link": "写入 .url Windows 互联网快捷方式。 操作系统基于文件路径缓存 URL",
  "--write-webloc-link": "写入 .webloc macOS 互联网快捷方式",
  "--xattr-set-filesize": "设置文件扩展属性 ytdl.filesize 为预期文件大小",
  "--xattrs": "使用 Dublin Core 和 XDG 标准将元数据写入视频文件的 xattrs",
  "--xff": "如何伪造 X-Forwarded-For HTTP 头以尝试 绕过地理限制。可以是“default”（仅在已知有用时）、 “never”、CIDR 表示法中的 IP 块， 或两个字母的 ISO 3166-2 国家代码",
  "--yes-playlist": "如果网址指向视频和播放列表，则下载播放列表",
  "-2": "双因素认证代码",
  "-4": "通过 IPv4 进行所有连接",
  "-6": "通过 IPv6 进行所有连接",
  "-F": "列出每个视频的可用格式。 除非使用 --no-simulate，否则模拟",
  "-I": "要下载的项目的逗号分隔的 playlist_index。 您可以使用“[起始]:[结束][:步长]”指定范围。 为了向后兼容，也支持 START-STOP。 使用负索引从右边计数，使用负 STEP 以相反顺序下载。 例如，在大小为 15 的播放列表上使用“-I 1:3,7,-5::2” 将下载索引为 1,2,3,7,11,13,15 的项目",
  "-J": "安静，但为每个传递的 URL 或 infojson 打印 JSON 信息。 除非使用 --no-simulate，否则模拟。 如果 URL 指向播放列表，则整个播放列表信息 在一行中转储",
  "-N": "应并发下载的 dash/hlsnative 视频的片段数 （默认为 1）",
  "-O": "要打印到屏幕的字段名称或输出模板， 可选择性地以打印时机为前缀，以“:”分隔。 “WHEN”的支持值与 --use-postprocessor 相同 （默认：video）。隐含 --quiet。 除非使用 --no-simulate 或 WHEN 的后期阶段，否则隐含 --simulate。 此选项可多次使用",
  "-P": "文件应下载到的路径。 指定文件类型和路径，以冒号“:”分隔。 支持与 --output 相同的所有类型。 此外，您还可以提供“home”（默认）和“temp”路径。 所有中间文件首先下载到临时路径， 然后在下载完成后将最终文件移动到主路径。 如果 --output 是绝对路径，则忽略此选项",
  "-R": "重试次数（默认为 10），或“infinite”",
  "-S": "按给定字段对格式进行排序， 详情请参阅“排序格式”",
  "-U": "将此程序更新至最新版本",
  "-a": "包含要下载的网址的文件（“-”表示标准输入）， 每行一个网址。以“#”、“;”或“]”开头的行被视为注释并被忽略",
  "-c": "恢复部分下载的文件/片段（默认）",
  "-f": "视频格式代码，详情请参阅“格式选择”",
  "-h": "打印此帮助文本并退出",
  "-i": "忽略下载和后处理错误。 即使后处理失败，下载也会被视为成功",
  "-j": "安静，但为每个视频打印 JSON 信息。 除非使用 --no-simulate，否则模拟。 有关可用键的描述，请参阅“输出模板”",
  "-k": "后处理后在磁盘上保留中间视频文件",
  "-n": "使用 .netrc 认证数据",
  "-o": "输出文件名模板；详情请参阅“输出模板”",
  "-p": "帐户密码。如果省略此选项， yt-dlp 将交互式询问",
  "-q": "激活安静模式。如果与 --verbose 一起使用， 则将日志打印到 stderr",
  "-r": "最大下载速率（字节/秒），例如 50K 或 4.2M",
  "-s": "不下载视频，也不向磁盘写入任何内容",
  "-t": "应用预定义的选项集。例如 --preset-alias mp3。 以下预设可用：mp3, aac, mp4, mkv, sleep。 更多信息请参阅末尾的“预设别名”部分。 此选项可多次使用",
  "-u": "使用此帐户 ID 登录",
  "-v": "打印各种调试信息",
  "-w": "不覆盖任何文件",
  "-x": "将视频文件转换为纯音频文件 （需要 ffmpeg 和 ffprobe）",
  "-最大": "等待预定的流变为可用。 传递重试之间等待的最小秒数（或范围）"
}
# END GENERATED OPTION TRANSLATIONS


MANUAL_OPTION_TRANSLATIONS = {
    '--js-runtimes': (
        '启用额外的 JavaScript 运行时，可指定其路径（可执行文件路径或所在目录）。'
        '默认可用的运行时包括 deno、node、bun 和 quickjs。此选项可多次使用'
    ),
    '--no-js-runtimes': (
        '清除要启用的 JavaScript 运行时，包括默认运行时及此前通过 '
        '--js-runtimes 添加的运行时'
    ),
    '--remote-components': (
        '允许 yt-dlp 在需要时获取远程组件。默认值包含全部远程组件'
    ),
    '--no-remote-components': (
        '禁止获取任何远程组件，包括此前通过 --remote-components 允许的组件'
    ),
    '--format-sort-reset': '忽略此前指定的格式排序规则并恢复默认排序',
    '--extractor-retries': (
        '已知提取器错误的重试次数（默认为 %default），或使用 “infinite” '
        '表示无限重试'
    ),
    '--allow-dynamic-mpd': (
        '处理动态 DASH 清单（默认；别名：--no-ignore-dynamic-mpd）'
    ),
    '--ignore-dynamic-mpd': (
        '不处理动态 DASH 清单（别名：--no-allow-dynamic-mpd）'
    ),
    '--hls-split-discontinuity': (
        '在广告中断等不连续点处，将 HLS 播放列表拆分为不同格式'
    ),
    '--no-hls-split-discontinuity': (
        '不在广告中断等不连续点处拆分 HLS 播放列表（默认）'
    ),
    '--extractor-args': (
        '将参数传递给指定的 IE_KEY 提取器。详情请参阅“提取器参数”；'
        '此选项可多次使用，以分别设置不同提取器的参数'
    ),
}


GROUP_TRANSLATIONS = {
    'General Options': '通用选项',
    'Network Options': '网络选项',
    'Geo-restriction': '地理限制',
    'Video Selection': '视频选择',
    'Download Options': '下载选项',
    'Filesystem Options': '文件系统选项',
    'Thumbnail Options': '缩略图选项',
    'Internet Shortcut Options': '互联网快捷方式选项',
    'Verbosity and Simulation Options': '详细输出与模拟选项',
    'Workarounds': '兼容与变通选项',
    'Video Format Options': '视频格式选项',
    'Subtitle Options': '字幕选项',
    'Authentication Options': '身份验证选项',
    'Post-Processing Options': '后处理选项',
    'SponsorBlock Options': 'SponsorBlock 选项',
    'Extractor Options': '提取器选项',
    'Aliases': '自定义别名',
    'Preset Aliases': '预设别名',
}


HELP_TEXT_TRANSLATIONS = {
    'Usage:': '用法：',
    'Options:': '选项：',
    '[OPTIONS] URL [URL...]': '[选项] 网址 [网址...]',
    'See full documentation at  https://github.com/yt-dlp/yt-dlp#readme':
        '完整文档：https://github.com/yt-dlp/yt-dlp#readme',
}


PRESET_DESCRIPTION_RE = re.compile(
    r'Predefined aliases for convenience and ease of use\.\s+Note that future\s+'
    r'versions of yt-dlp may add or adjust presets, but the existing preset\s+'
    r'names will not be changed or removed')


MESSAGE_PATTERNS = (
    (re.compile(r'^\[download\] Destination: (.+)$'), r'[下载] 目标文件：\1'),
    (re.compile(r'^\[download\] (.+) has already been downloaded$'),
     r'[下载] \1 已下载，跳过'),
    (re.compile(r'^\[download\] The file has already been downloaded$'),
     '[下载] 文件已下载，跳过'),
    (re.compile(r'^\[download\] Deleting existing file(?: (.+))?$'),
     r'[下载] 正在删除已有文件\1'),
    (re.compile(r'^\[download\] Finished downloading playlist: (.+)$'),
     r'[下载] 播放列表下载完成：\1'),
    (re.compile(r'^\[download\] Downloading playlist: (.+)$'),
     r'[下载] 正在下载播放列表：\1'),
    (re.compile(r'^\[download\] Downloading item (\d+) of (\d+)$'),
     r'[下载] 正在下载第 \1 项，共 \2 项'),
    (re.compile(r'^\[download\] Downloading (.+)$'), r'[下载] 正在下载 \1'),
    (re.compile(r'^\[download\] ([\d.]+%) of ~?(.+) at (.+) ETA (.+)$'),
     r'[下载] 已完成 \1，共 ~\2，速度 \3，预计剩余 \4'),
    (re.compile(r'^\[download\] ([\d.]+%) at (.+) ETA (.+)$'),
     r'[下载] 已完成 \1，速度 \2，预计剩余 \3'),
    (re.compile(r'^\[download\] ([\d.]+%) of ~?(.+) at (.+)$'),
     r'[下载] 已完成 \1，共 ~\2，速度 \3'),
    (re.compile(r'^\[info\] Writing (.+) to: (.+)$'),
     r'[信息] 正在写入 \1 到：\2'),
    (re.compile(r'^\[info\] Downloading (.+)$'), r'[信息] 正在下载 \1'),
    (re.compile(r'^\[info\] Testing format (.+)$'),
     r'[信息] 正在测试格式 \1'),
    (re.compile(r'^\[info\] Available (.+) for (.+):$'),
     r'[信息] \2 可用的 \1：'),
    (re.compile(r'^\[info\] There are no subtitles for the requested languages$'),
     '[信息] 所请求语言没有可用字幕'),
    (re.compile(r'^\[info\] There are no (.+) thumbnails to download$'),
     r'[信息] 没有可下载的 \1 缩略图'),
    (re.compile(r'^\[info\] Skipping writing video subtitles$'),
     '[信息] 跳过写入视频字幕'),
    (re.compile(r'^\[Merger\] Merging formats into "(.+)"$'),
     r'[合并器] 正在将格式合并为“\1”'),
    (re.compile(r'^\[Metadata\] (.+)$'), r'[元数据] \1'),
    (re.compile(r'^\[wait\] Waiting for (.+) - Press Ctrl\+C to try now$'),
     r'[等待] 正在等待 \1，按 Ctrl+C 立即重试'),
    (re.compile(r'^ERROR: (.+)$'), r'错误：\1'),
    (re.compile(r'^WARNING: (.+)$'), r'警告：\1'),
    (re.compile(r'^Extracting URL: (.+)$'), r'正在提取网址：\1'),
    (re.compile(r'^Downloading webpage$'), '正在下载网页'),
    (re.compile(r'^Downloading API JSON$'), '正在下载 API JSON'),
    (re.compile(r'^Downloading player (.+)$'), r'正在下载播放器 \1'),
    (re.compile(r'^Postprocessing: (.+)$'), r'正在后处理：\1'),
    (re.compile(r'^Finished downloading playlist: (.+)$'),
     r'播放列表下载完成：\1'),
)


PREFIX_TRANSLATIONS = (
    ('[download]', '[下载]'),
    ('[info]', '[信息]'),
    ('[debug]', '[调试]'),
    ('[warning]', '[警告]'),
    ('[error]', '[错误]'),
)


FALLBACK_PHRASES = (
    ('Check if updates are available.', '检查是否有可用更新。'),
    ('Update this program to the latest', '将此程序更新至最新的'),
    ('Do not check for updates', '不检查更新'),
    ('default', '默认'),
    ('Alias:', '别名：'),
    ('Default:', '默认值：'),
    ('Supported values:', '支持的值：'),
    ('Currently supported:', '当前支持：'),
    ('This option can be used multiple times', '此选项可多次使用'),
    ('Use this option multiple times', '此选项可多次使用'),
    ('Enable', '启用'),
    ('Disable', '禁用'),
    ('Do not', '不要'),
    ('Print', '显示'),
    ('Download', '下载'),
    ('Location of', '位置：'),
    ('Path to', '路径：'),
)


def _enabled():
    return os.environ.get('YT_DLP_LANG', '').lower() not in ('en', 'en-us', 'c')


def _configure_redirected_output():
    """Use UTF-8 for redirected output, independent of the runner locale."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'isatty') and not stream.isatty() and hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8', errors='replace')


def _translate_fallback_help(text):
    result = text
    for source, target in FALLBACK_PHRASES:
        result = result.replace(source, target)
    return result


def _translate_option_help(option):
    current = getattr(option, 'help', None)
    if not current or not isinstance(current, str):
        return

    for flag in (*option._long_opts, *option._short_opts):
        if translated := MANUAL_OPTION_TRANSLATIONS.get(flag):
            option.help = translated
            return
        if translated := OPTION_TRANSLATIONS.get(flag):
            option.help = translated
            return

    option.help = _translate_fallback_help(current)


def translate_message(message):
    if not _enabled() or not isinstance(message, str):
        return message

    result = message
    for pattern, replacement in MESSAGE_PATTERNS:
        result = pattern.sub(replacement, result)
    for source, target in PREFIX_TRANSLATIONS:
        result = result.replace(source, target)
    return result


def translate_help(text):
    if not _enabled() or not isinstance(text, str):
        return text

    result = text
    for source, target in sorted(
            GROUP_TRANSLATIONS.items(), key=lambda item: len(item[0]), reverse=True):
        result = result.replace(source, target)
    for source, target in HELP_TEXT_TRANSLATIONS.items():
        result = result.replace(source, target)
    result = PRESET_DESCRIPTION_RE.sub(
        '为便于使用而预定义的别名。未来版本可能新增或调整预设，但现有预设名称'
        '不会被更改或移除',
        result)

    result = result.replace('Usage:', '用法：')
    result = result.replace(' (default:', '（默认：')
    result = re.sub(r'\(Alias: ([^)]+)\)', r'（别名：\1）', result)
    return result


def install():
    _configure_redirected_output()
    if not _enabled():
        return

    from yt_dlp.YoutubeDL import YoutubeDL
    from yt_dlp.options import _YoutubeDLOptionParser

    original_format_help = _YoutubeDLOptionParser.format_help
    original_to_screen = YoutubeDL.to_screen

    def format_help(self):
        for group in (self, *self.option_groups):
            for option in group.option_list:
                _translate_option_help(option)
        return translate_help(original_format_help(self))

    def to_screen(self, message, *args, **kwargs):
        return original_to_screen(self, translate_message(message), *args, **kwargs)

    _YoutubeDLOptionParser.format_help = format_help
    YoutubeDL.to_screen = to_screen


install()
