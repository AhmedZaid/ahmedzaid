

def create_quotes(cur, new_content, new_author_name, new_tags):
    new_content = "'" + new_content + "'"
    new_author_name = "'" + new_author_name + "'"
    new_tags = "'" + new_tags + "'"

    sql = f"INSERT INTO quotesdb.quotes(content, author_name, tags) VALUES ({new_content}, {new_author_name}, {new_tags});"
    cur.execute(sql)
