/**
 * 北京2026高考志愿填报 - 数据模型
 * 数据来源：北京教育考试院、阳光高考平台
 */

// 招生批次
const BATCH_TYPES = {
  GAOKAO: '高考',
  ZHIJIAO: '高职单招',
};

// 选科组合类型
const SUBJECT_COMBINATIONS = {
  WENKE: '文科组（史地政）',
  LIKE: '理科组（物化生）',
  WENKE_DALITU: '文理兼收',
};

// 院校层次
const SCHOOL_LEVELS = {
  QIANJIAN: '强基计划',
  ZIXIAO: '985/211',
  YIBAN: '一本',
  ERBAN: '二本',
  ZHUANKE: '专科',
};

/**
 * 专业组
 * @typedef {Object} MajorGroup
 * @property {string} id - 专业组ID
 * @property {string} schoolName - 学校名称
 * @property {string} schoolCode - 学校代码
 * @property {string} groupCode - 专业组代码
 * @property {string} groupName - 专业组名称
 * @property {string} batch - 招生批次
 * @property {string} level - 院校层次
 * @property {string} subjectRequirement - 选科要求
 * @property {Major[]} majors - 专业列表
 * @property {number} planNum - 招生计划数
 * @property {number} minScore - 最低录取分（历史数据）
 * @property {number} minRank - 最低录取位次（历史数据）
 */

/**
 * 专业
 * @typedef {Object} Major
 * @property {string} code - 专业代码
 * @property {string} name - 专业名称
 * @property {string} type - 专业类型（普通/艺术/体育）
 * @property {number} tuition - 学费
 * @property {number} years - 学制
 */

/**
 * 历史录取数据
 * @typedef {Object} AdmissionRecord
 * @property {string} year - 年份
 * @property {string} schoolName - 学校名称
 * @property {string} groupName - 专业组名称
 * @property {string} batch - 批次
 * @property {number} score - 录取分数
 * @property {number} rank - 录取位次
 * @property {number} planNum - 招生计划
 * @property {number} actualNum - 实际录取
 */

/**
 * 考生输入
 * @typedef {Object} StudentProfile
 * @property {number} totalScore - 高考总分
 * @property {number} chinese - 语文
 * @property {number} math - 数学
 * @property {number} english - 英语
 * @property {string[]} subjects - 选考科目
 * @property {string} location - 户籍所在地
 */

module.exports = {
  BATCH_TYPES,
  SUBJECT_COMBINATIONS,
  SCHOOL_LEVELS,
};
