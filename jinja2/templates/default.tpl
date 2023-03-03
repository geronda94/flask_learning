<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tiutle</title>
</head>
<body>
    {% block content %}
        {% block table_contents %}
        <ul>
        {% for li in list_table -%}
        <li> {{ li }} </li>
        {% endfor -%}
        </ul>
        {% endblock table_contents %}
    {% endblock content %}
    <h1>555</h1>


</body>
</html>