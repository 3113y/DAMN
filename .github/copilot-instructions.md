# DAMN - Keep Talking and Nobody Explodes 单人通关手册

这是一个使用 PyQt5 构建的《Keep Talking and Nobody Explodes》游戏的单人辅助工具，为各种炸弹模块提供解题算法。

## 架构概览

- **主入口**: `Damn/Damn.py` - 包含 PyQt5 GUI 应用和主菜单逻辑
- **模块文件**: `Damn/scripts/` - 各个炸弹模块的独立实现文件
- **项目结构**: 支持 Visual Studio Python 项目 (`.pyproj`) 和现代 Python 项目 (`pyproject.toml`)
- **资源文件**: `Damn/pictures/` - 迷宫模块的解题图片资源 (按坐标命名: `11.jpg`, `13.jpg` 等)

## 模块系统

应用采用模块化架构，主文件负责 GUI 框架和模块选择，各个炸弹模块实现为独立文件：

### 核心模块文件
- `scripts/line_module.py` - 线路模块：基于线的颜色和序列号实现复杂的决策算法
- `scripts/button_module.py` - 按钮模块：考虑按钮颜色、文字、电池数和指示灯状态
- `scripts/four_color_block_module.py` - 四色方块模块：基于序列号是否含元音字母
- `scripts/memory_module.py` - 记忆模块：5阶段记忆算法，跟踪位置和数字
- `scripts/maze_module.py` - 迷宫模块：交互式网格选择，动态加载对应图片

### 模块导入结构
```python
# 主文件 Damn.py 中的导入
from scripts.line_module import line_module
from scripts.button_module import button_module
from scripts.four_color_block_module import four_color_block_module
from scripts.memory_module import memory_module
from scripts.maze_module import maze_module
```

### 数据结构模式
```python
# 线路模块使用数组编码颜色: [0=无, 1=白, 2=红, 3=黄, 4=蓝, 5=黑]
strs_arr = [0] * 6
strs_num_sum = [0] * 6  # 颜色计数器

# 记忆模块跟踪状态
rem_stage = [0] * 5      # 大屏数字
rem_stage_site = [0] * 5 # 按下位置
rem_stage_scre = [0] * 5 # 按下数字
```

## 关键技术实现

### PyQt5 交互模式
- 使用 `QMessageBox` 创建自定义按钮组合进行用户选择
- 通过 `QInputDialog.getInt()` 获取数值输入
- 使用 `QMessageBox.question()` 进行是/否确认

### 图片加载模式
```python
# 迷宫模块图片命名规则: 根据第一个标识的坐标确定 (如: (1,1) → "11.jpg")
file_name = f"pictures\\{pic_name}.jpg"
```

### 坐标系统
- 用户界面显示1-based坐标 `(1,1)` 到 `(6,6)`
- 内部存储使用1-based坐标进行图片映射
- 图片文件命名基于第一个标识点的行列坐标

### 状态管理
- 迷宫模块使用类属性 `mark_site` 和 `maze_click_count` 跟踪点击状态
- 每个模块完成后必须调用 `parent.switch_module()` 返回主菜单（注意括号！）
- 迷宫模块显示图片后提供"返回主菜单"按钮
- 所有用户取消操作都应正确处理并返回主菜单

## 开发约定

### 算法实现
- 所有游戏逻辑都基于官方 Keep Talking and Nobody Explodes 规则手册
- 使用数值编码而非字符串提高处理效率
- 复杂条件判断使用嵌套 if-elif 结构保持清晰

### 用户体验
- 所有交互使用中文界面
- 提供清晰的步骤提示和结果显示
- 支持取消操作和错误处理

### 文件组织
- 主逻辑集中在 `Damn.py` 便于维护，各模块分离为独立文件
- 各模块实现在 `scripts/` 目录下的独立文件中
- 图片资源按功能分组在 `pictures/` 目录
- 支持 Visual Studio 和现代 Python 工具链

## 运行和调试

### 启动应用
```bash
cd Damn
python Damn.py
```

### 依赖要求
- PyQt5 (GUI框架)
- Python 3.9+ (根据 pyproject.toml)

### Visual Studio 支持
- 项目配置: `Damn.pyproj` 和 `Damn.sln`
- 启动文件: `Damn.py`
- 调试模式支持

## 常见问题和修复

### UI 流程问题
- **空白UI问题**: 确保所有模块方法末尾调用 `parent.switch_module()` 而不是 `parent.switch_module`
- **用户取消处理**: 迷宫模块等需要特殊处理用户取消操作，避免显示空白窗口
- **迷宫模块特殊性**: 需要在图片显示完成后提供返回按钮，因为它改变了窗口布局
- **图片加载失败**: 
  - 使用 f-string 而不是原始字符串配合 .format()
  - 确保工作目录正确（在 Damn/ 目录下运行）
  - 坐标映射要考虑界面显示的1-based和内部逻辑的对应关系

## 扩展新模块

添加新炸弹模块时遵循以下模式：
1. 在 `switch_module()` 中添加新按钮
2. 在 `scripts/` 目录创建新的模块文件
3. 在主文件中添加对应的导入语句
4. 实现用户输入收集和算法逻辑
5. 调用 `parent.switch_module()` 返回主菜单
6. 如需图片资源，放置在 `pictures/` 目录并遵循命名规则