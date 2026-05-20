#!/usr/bin/env python3
"""
北京高考志愿数据采集脚本
数据来源：
- 北京教育考试院：https://www.bjeea.cn
- 阳光高考平台：https://gaokao.chsi.com.cn
- 北京考试报

注意：本脚本提供数据采集框架框架，实际数据需要从官方渠道获取并手动整理
"""

import requests
import json
import time
import re
from pathlib import Path

# 配置
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

class BeijingGaokaoDataCollector:
    """北京高考数据采集器"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.base_dir = Path(__file__).parent.parent
        self.data_dir = self.base_dir / 'data' / 'raw'
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def fetch_bjeea_plan(self):
        """获取北京教育考试院招生计划数据"""
        # 计划查询API
        url = "http://query.bjeea.cn/queryService/rest/plan/115"
        try:
            resp = self.session.get(url, timeout=10)
            resp.encoding = 'utf-8'
            print(f"[北京考试院] 招生计划查询: {resp.status_code}")
            return resp.text
        except Exception as e:
            print(f"[错误] 获取招生计划失败: {e}")
            return None
    
    def fetch_bjeea_admission_stats(self):
        """获取北京教育考试院录取统计（2022-2024）"""
        # 考生服务系统URL
        url = "https://gk-stu.bjeea.cn"
        try:
            resp = self.session.get(url, timeout=10)
            print(f"[北京考试院] 考生服务系统: {resp.status_code}")
            return resp.text
        except Exception as e:
            print(f"[错误] 获取录取统计失败: {e}")
            return None
    
    def fetch_ygkzy_major_list(self):
        """获取阳光高考专业库"""
        # 专业库API
        url = "https://gaokao.chsi.com.cn/zyk/zybk/zyzl.jsp"
        try:
            resp = self.session.get(url, timeout=10)
            resp.encoding = 'utf-8'
            print(f"[阳光高考] 专业库: {resp.status_code}")
            return resp.text
        except Exception as e:
            print(f"[错误] 获取专业库失败: {e}")
            return None
    
    def save_data(self, filename, content):
        """保存数据到文件"""
        filepath = self.data_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[保存] {filepath}")
    
    def run(self):
        """运行采集"""
        print("=" * 50)
        print("北京高考志愿数据采集")
        print("=" * 50)
        
        # 获取各项数据
        print("\n[1/3] 获取北京教育考试院招生计划...")
        plan_data = self.fetch_bjeea_plan()
        
        print("\n[2/3] 获取北京教育考试院录取统计...")
        stats_data = self.fetch_bjeea_admission_stats()
        
        print("\n[3/3] 获取阳光高考专业库...")
        major_data = self.fetch_ygkzy_major_list()
        
        # 保存原始数据
        if plan_data:
            self.save_data('bjeea_plan.html', plan_data)
        if stats_data:
            self.save_data('bjeea_stats.html', stats_data)
        if major_data:
            self.save_data('ygkzy_majors.html', major_data)
        
        print("\n" + "=" * 50)
        print("采集完成！")
        print("注意：这些是原始网页数据，需要进一步解析提取结构化数据")
        print("=" * 50)

if __name__ == '__main__':
    collector = BeijingGaokaoDataCollector()
    collector.run()
