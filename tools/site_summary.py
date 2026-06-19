class SiteProfile:
    def __init__(self, name, url, keywords, tags, description):
        self.name = name
        self.url = url
        self.keywords = keywords
        self.tags = tags
        self.description = description

    def summary(self):
        kw_str = ", ".join(self.keywords)
        tag_str = ", ".join(self.tags)
        return (
            f"站点名称: {self.name}\n"
            f"URL: {self.url}\n"
            f"关键词: {kw_str}\n"
            f"标签: {tag_str}\n"
            f"说明: {self.description}\n"
        )


def load_sample_sites():
    return [
        SiteProfile(
            name="爱游戏门户",
            url="https://app-portal-i-game.com.cn",
            keywords=["爱游戏", "游戏平台", "手游", "综合游戏"],
            tags=["portal", "games", "mobile", "娱乐"],
            description="爱游戏官方门户，提供丰富的手机游戏下载与资讯服务。"
        ),
        SiteProfile(
            name="游戏社区",
            url="https://bbs.example.com",
            keywords=["社区", "讨论", "攻略"],
            tags=["forum", "social", "玩家"],
            description="玩家交流社区，分享游戏心得与攻略。"
        ),
        SiteProfile(
            name="游戏资讯站",
            url="https://news.example.com",
            keywords=["资讯", "新游", "评测"],
            tags=["news", "reviews", "更新"],
            description="最新游戏资讯、评测和活动信息。"
        )
    ]


def generate_summary_report(sites):
    lines = []
    lines.append("=" * 48)
    lines.append("         站点资料结构化摘要")
    lines.append("=" * 48)
    for idx, site in enumerate(sites, 1):
        lines.append(f"\n--- 站点 {idx} ---")
        lines.append(site.summary())
    lines.append("=" * 48)
    lines.append("摘要结束")
    return "\n".join(lines)


def export_report_to_file(content, filename="site_summary_output.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


def run_demo():
    sites = load_sample_sites()
    report = generate_summary_report(sites)
    print(report)
    export_report_to_file(report)
    print("摘要已写入 site_summary_output.txt")


if __name__ == "__main__":
    run_demo()