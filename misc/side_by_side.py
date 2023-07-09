https://stackoverflow.com/questions/38783027/jupyter-notebook-display-two-pandas-tables-side-by-side


Aug 6, 2016 at 8:03	zarak
Jun 17, 2018 at 18:08	gibbone
Sep 7, 2019 at 8:29	Anton Golubev
Jul 20, 2021 at 6:01	Rich Lysakowski PhD


# Anton Golubev
from IPython.core.display import display, HTML

def display_side_by_side(dfs:list, captions:list):
    """Display tables side by side to save vertical space
    Input:
        dfs: list of pandas.DataFrame
        captions: list of table captions
    """
    output = ""
    combined = dict(zip(captions, dfs))
    for caption, df in combined.items():
        output += df.style.set_table_attributes("style='display:inline'").set_caption(caption)._repr_html_()
        output += "\xa0\xa0\xa0"
    display(HTML(output))

# Usage:
display_side_by_side([df1, df2, df3], ['caption1', 'caption2', 'caption3'])


# Rich Lysakowski PhD
from IPython.core.display import display, HTML

def display_side_by_side(dfs:list, captions:list, tablespacing=5):
    """Display tables side by side to save vertical space
    Input:
        dfs: list of pandas.DataFrame
        captions: list of table captions
    """
    output = ""
    for (caption, df) in zip(captions, dfs):
        output += df.style.set_table_attributes("style='display:inline'").set_caption(caption)._repr_html_()
        output += tablespacing * "\xa0"
    display(HTML(output))

# Usage:
display_side_by_side([df1, df2, df3], ['caption1', 'caption2', 'caption3'])

# Ровно та же функция, только добавлен tablespacing

