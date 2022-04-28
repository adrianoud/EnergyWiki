from flask import Flask, render_template, request, jsonify, redirect, url_for, json
from energy_model import Primary_Energy_Consumption
from pyecharts import options as opts
from pyecharts.charts import Line, Map, Bar


app = Flask(__name__)
app.secret_key = 'development key'
app.config['JSON_AS_ASCII'] = False

PMC = Primary_Energy_Consumption()
# 需要在html中额外导入地图js文件 , 需要进行地图名称映射
Name_Map_Data = {"United States": "US", "Russia": "Russian Federation", "Korea": "South Korea"}


def line_base(regions) -> Line:
    c = Line()
    c.add_xaxis([str(year) for year in PMC.get_years()])  # 仅支持字符串
    for region in regions:
        c.add_yaxis(region, PMC.get_data(region))
    c.set_global_opts(title_opts=opts.TitleOpts(title="分区域一次能源消耗趋势", subtitle="单位：EJ"),
                      toolbox_opts=opts.ToolboxOpts(is_show=True)
                      )
    return c


def bar_base(year) -> Bar:
    c = Bar()
    temp = PMC.get_year_top10(year)
    c.add_xaxis(list(temp.index))
    c.add_yaxis(str(year)+"年消耗前10国家或地区", list(temp))
    return c


def map_base(year) -> Map:
    c = Map()
    num = PMC.get_year_data(year)
    country = PMC.get_region_list()
    c.add("YearlyPrimaryEnergy", [list(z) for z in zip(country, num)], "world", is_map_symbol_show=False, is_roam=False,
          name_map=Name_Map_Data)
    c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title=str(year) + "年各国家一次能源消耗"),
        visualmap_opts=opts.VisualMapOpts(max_=80),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    return c


@app.route('/')
def index():
    region_list = PMC.get_region_list()
    year_list = PMC.get_years()
    return render_template("index.html", region_list=region_list, year_list=year_list)


# controller 功能
@app.route("/Chart", methods=['GET', 'POST'])
def get_chart():
    regions = eval(request.form.get('region'))
    c = line_base(regions)
    return c.dump_options_with_quotes()


@app.route("/Map", methods=['GET', 'POST'])
def get_map():
    year = int(request.form.get('year'))
    c = map_base(year)
    return c.dump_options_with_quotes()


@app.route("/Bar", methods=['GET', 'POST'])
def get_bar():
    year = int(request.form.get('year'))
    c = bar_base(year)
    return c.dump_options_with_quotes()


if __name__ == '__main__':
    app.config['JSONIFY_MIMETYPE'] = "application/json; charset=utf-8"
    app.run(debug=True)
