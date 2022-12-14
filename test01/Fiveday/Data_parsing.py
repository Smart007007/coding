"""
一、解析xml     xml树结构的标签语言，xml自身提供数据解析库dom
    1、定位文件
    2、打开文件
    3、解析文件
    4、返回数据
二、解析Yaml   文本语言，三方库yaml进行解析
    1、定位文件
    2、打开文件
    3、返回数据
"""
#定义数据解析类
class Data_parsing:
    # 定义解析xml数据方法
    def analysis_xml(self,firstTag,secondTag):
        from xml.dom import minidom
        # 定位文件
        xmlfile='../poolData/xmlData.xml'
        #打开文件
        openfile=minidom.parse(xmlfile)
        # 定位一级标签
        OneNode=openfile.documentElement.getElementsByTagName(firstTag)[0]
        #定位二级标签
        TwoNode=OneNode.getElementsByTagName(secondTag)[0]
        #获取元素的第一个子元素节点值并返回
        return TwoNode.childNodes[0].nodeValue
    # 定义解析Yaml数据方法
    def analysis_Yaml(self):
        import yaml
        yamlFile="../poolData/yamlData.yml"
        f=open(yamlFile)
        return yaml.safe_load(f)

analysis=Data_parsing()
print(analysis.analysis_xml("todo", "sex"))
print(analysis.analysis_Yaml())



