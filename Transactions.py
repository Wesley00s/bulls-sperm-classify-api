import psycopg2


#
# def get_data_to_classify():
#     try:
#         conn = psycopg2.connect(
#             dbname="railway",
#             user="postgres",
#             password="CArBbfxiDbtRNuZVSCeMVQMEJZeMeCDk",
#             host="viaduct.proxy.rlwy.net",
#             port="16546"
#         )
#
#         cursor = conn.cursor()
#
#         cursor.execute('''SELECT * FROM DATA_VIEW ORDER BY id DESC LIMIT 1;''')
#
#         column_names = [desc[0] for desc in cursor.description]
#
#         result = cursor.fetchall()
#
#         rows_as_dicts = [dict(zip(column_names, row)) for row in result]
#
#         json_result = json.dumps(rows_as_dicts)
#         json_result = json.loads(json_result)
#         print("Data fetched from 'DATA_VIEW' table:")
#         print(json_result)
#
#         cursor.close()
#         conn.close()
#
#         return json_result[0]
#     except Exception as e:
#         print("An error occurred while fetching data from 'DATA_VIEW' table:", e)
#         return None

#
# def add_data_classify(alvo):
#     conn = psycopg2.connect(
#         dbname="railway",
#         user="postgres",
#         password="CArBbfxiDbtRNuZVSCeMVQMEJZeMeCDk",
#         host="viaduct.proxy.rlwy.net",
#         port="16546"
#     )
#
#     cursor = conn.cursor()
#
#     data = get_data_to_classify()
#
#     data.update({"alvo": alvo})
#     data.pop("id")
#
#     values = tuple(data.values())
#
#     sql = '''INSERT INTO DATA_CLASSIFY (idade, peso, ec, ce, temp_retal, temp_amb, umidade, mov_flanco, turbilhao,
#                       mot_moveis, vigor, volume, zptz_106, zptz_totais, def_mai, def_mai_percent, def_men, def_men_percent,
#                       normais, normais_percent, alvo)
#                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
#
#     cursor.execute(sql, values)
#
#     conn.commit()
#     cursor.close()
#     conn.close()
#

def add_data(data):
    print(data)
    data = dict(data)

    conn = psycopg2.connect(
        dbname="railway",
        user="postgres",
        password="CArBbfxiDbtRNuZVSCeMVQMEJZeMeCDk",
        host="viaduct.proxy.rlwy.net",
        port="16546"
    )

    cursor = conn.cursor()

    values = tuple(data.values())

    sql = '''INSERT INTO DATA_CLASSIFY (idade, peso, ec, ce, temp_retal, temp_amb, umidade, mov_flanco, turbilhao,
                      mot_moveis, vigor, volume, zptz_106, zptz_totais, def_mai, def_mai_percent, def_men, def_men_percent,
                      normais, normais_percent, alvo)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''

    cursor.execute(sql, values)

    conn.commit()
    cursor.close()
    conn.close()

#
# def get_data():
#     conn = psycopg2.connect(
#         dbname="railway",
#         user="postgres",
#         password="CArBbfxiDbtRNuZVSCeMVQMEJZeMeCDk",
#         host="viaduct.proxy.rlwy.net",
#         port="16546"
#     )
#     cursor = conn.cursor()
#
#     data = pd.read_sql("SELECT * FROM DATA_CLASSIFY;", conn)
#     print("Data get by 'DATA_CLASSIFY' table")
#     print(data)
#
#     cursor.close()
#     conn.close()
#
#     return data
