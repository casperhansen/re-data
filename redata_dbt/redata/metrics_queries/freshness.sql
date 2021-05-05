
{% set tables =  run_query(get_tables()) %}

{% for mtable in tables %}

    select
        {{current_timestamp()}},
        {{current_timestamp()}} - max({{mtable['time_filter']}}) as freshness,
        '{{mtable['full_table_name']}}' as table

    from
        {{mtable['full_table_name']}}
    where
        {{mtable['time_filter']}} < {{ time_window_end() }}

{% if not loop.last -%} union all {%- endif %}
{% endfor %}