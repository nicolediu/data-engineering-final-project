with orders as (
    select * from {{ ref('stg_olist__orders') }}
),

customers as (
    select * from {{ ref('stg_olist__customers') }}
),

final as (
    select
        o.order_id,
        o.customer_id,
        o.order_status,
        o.purchased_at,
        c.customer_city,
        c.customer_state
    from orders o
    left join customers c on o.customer_id = c.customer_id
)

select * from final