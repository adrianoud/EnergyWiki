from flask import Flask, render_template, request, jsonify, redirect, url_for, json
from energy_model import Primary_Energy_Consumption
from pyecharts import options as opts
from random import randrange
from pyecharts.charts import Line


app = Flask(__name__)
app.secret_key = 'development key'
app.config['JSON_AS_ASCII'] = False

PMC = Primary_Energy_Consumption()


def line_base(regions) -> Line:
    c = Line()
    c.add_xaxis([str(year) for year in PMC.get_years()])        # 仅支持字符串
    for region in regions:
        c.add_yaxis(region, PMC.get_data(region))
    c.set_global_opts(title_opts=opts.TitleOpts(title="一次能耗分区域趋势图", subtitle="regions"))
    return c


@app.route('/')
def index():
    region_list = PMC.get_region_list()
    return render_template("index.html", region_list=region_list)


@app.route("/Chart", methods=['GET', 'POST'])
def get_chart():
    regions = eval(request.form.get('region'))
    c = line_base(regions)
    return c.dump_options_with_quotes()


if __name__ == '__main__':
    app.config['JSONIFY_MIMETYPE'] = "application/json; charset=utf-8"
    app.run(debug=True)
