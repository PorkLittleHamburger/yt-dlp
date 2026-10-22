# yt-dlp 简体中文每日构建

这是 [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) 的简体中文再打包分支。
工作流会跟踪上游 **nightly** 发布，将对应源码提交同步到本仓库，并在不修改
站点解析逻辑的前提下加入简体中文运行时界面和帮助文本。

## 下载

打开本仓库的 [Releases](https://github.com/PorkLittleHamburger/yt-dlp/releases)
页面，下载：

- `yt-dlp.exe`：Windows 10+ x64 独立程序，不需要安装 Python。
- `yt-dlp_zh.exe`：同上，保留一个便于识别的中文版文件名。
- `SHA2-256SUMS`：下载文件的 SHA-256 校验值。
- `help-zh.txt`：该构建实际生成的简体中文帮助文本。

FFmpeg/ffprobe 未内置在单一 EXE 中；合并高画质音视频、转换格式、嵌入字幕和
封面等功能仍建议安装 FFmpeg。

## 自动同步

`.github/workflows/build-zh-cn.yml` 每 6 小时检查一次
`yt-dlp/yt-dlp-nightly-builds` 的最新发布：

1. 从 nightly 发布说明中解析精确的上游提交 SHA。
2. 拉取该提交并叠加本仓库的本地化层。
3. 在 Windows x64 环境构建单文件程序。
4. 验证中文帮助、版本号和可执行文件校验值。
5. 将同步后的源码推送到本仓库默认分支并创建同版本 Release。

相同上游版本不会在定时任务中重复发布；修改本地化文件或手动指定
`force` 时可以重建。

## 本地验证

```powershell
python localization/check_localization.py --require-complete
python -c "import importlib.util,sys; p=r'localization/zh_cn_runtime.py'; s=importlib.util.spec_from_file_location('zh_hook',p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); sys.argv=['yt-dlp','--help']; import yt_dlp; yt_dlp.main()"
```

设置 `YT_DLP_LANG=en` 可禁用中文运行时本地化，以便将问题与上游行为对比。

本项目遵循上游的许可和第三方依赖许可。该分支只增加本地化与 CI 构建代码。
