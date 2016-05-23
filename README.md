##Overview
---
 time:2016.3
* 检索方式：  
  通过cypher中match的语法，对query（已转化为cypher语句）在neo4j上进行检索，对得到的结果进行处理（排序等），和预置选项进行匹配，得到最终结果。关键：自然语言转为cypher查询语句
* 基础：  
 已存在预期的neu4j数据库
* 具体方式：  

  1. 对query进行分词、语义角色标注(依存分析)（借助niuparser等）
  2. 确定query的类别
	* 关键：把query分为两种形式（需要制定标准）：  
	  1. 实体的属性{attribute:key}  
	  2. 关系实体的元组-[:r{attribute:key}]->(e)  
  3. 使用match进行查询，得到结果（集合）
    * 关键：需要能进行同义词的匹配  

##Ver  0.1  
---
time:2016.4  
* change:  
  经过讨论，目前的数据库建库方式采用<e,r,e>,<r,“name”,value>的形式，即目前的数据库中node是不存在attribute的。
* 基础：  
	neo4j Document: http://neo4j.com/docs/2.3.3/
* 问句的分析：  
  1. 分词及词性分析
  2. 命名实体识别（地点，时间，人名等）
  3. 依存关系分析（主谓，动宾，修饰等）
  4. 语句分类（疑问词，限定域，开放域）
  5. 去冗余提取焦点词[focus word]
  6. 最终句子的组织方式
* 查询和相关API:  
  1. 问句表达式到cypher的转化
  2. 查询及返回
  3. 为后续分析编写设置API
	 
####前期尝试:  
* 语句处理阶段  
  1. 最初，我认为如果采用文法规则的方法去分析问句的话，需要使用一个文法分析效果比较好的工具。于是，我尝试了去使用nltk的一些库，但是在nltk中并没有找到关于已存分析的工具。
  2. 然后，我放弃了nltk，发现了工具HanLP,项目托管地址：https://github.com/hankcs/HanLP ，hanlp是主要针对java写的，所有需要导入jpype这个包，去实现在python中嵌入java。尝试后发现，hanlp在py下的工作状	态不如java，它的dp无法实现，但是其进行“摘要”的功能是不错的，可以留待后用。  
  3. 最终，我暂时使用了niuparse的相关功能。
* neo4j数据库链接阶段  
  1. 最初，进行了java的嵌入式尝试，效果还是不错的。具体实现可参见我的blog:http://blog.csdn.net/u014451076/article/details/50998957
  2. 接着，进行了python下的链接（最终个人希望是用py写一套系统）。开始的时候是参照官网给出的方式，http://neo4j.com/developer/ ，开始是成功实现的，后来个人电脑系统进行了升级，再次进行配置时，发现无法配	置成功。原因：使用bolt协议，这个协议只支持py2.7.9+和3.3+，但是本次自带的py是2.7.3和3.4，尝试手动进行py2.7.9的安装，但是安装neo4j-driver的过程需要使用pip，而pip的安装需要依赖py，而py的版本命令是取前两位（均为py2.7），没有找到相关的解决方案。最终	这种方法只能放弃，但是如果py版本正确，相关配置是可以实现的。
  3. 最终，选择了使用jpype和embeded进行py的开发。介绍和安装方法可简单参考：http://blog.csdn.net/dyllove98/article/details/8635965 和 http://docs.neo4j.org.cn/python-embedded.html
* 程序实现：
  代码托管在https://github.com/su526664687/NEUBAIDUNLP

##Ver 0.2  
---
time:2016.5
* change:  
  经过后期的讨论，现阶段决定使用统计的方法进行对query的处理。近期通读了《数学之美》，此书值得一读。在当今nlp界，自然语言处理从规则到统计已经成为一种必然的趋势。
* 基础：
  已经获取的三元组<s,r,e>
* 具体方式：
  1. 通过百度知道搜索s e的形式，收集到大量的“知道问题”，现阶段每个s e收集min(50,amount)
  2. 提取模板
* 文件位置：
 现阶段所有文件存储在172服务器~/sjming下	

