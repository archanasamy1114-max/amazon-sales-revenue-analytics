SELECT
    ROUND(SUM(CASE WHEN Is_Cancelled = 0 THEN Amount ELSE 0 END), 2) AS Total_Revenue,
    COUNT(DISTINCT CASE WHEN Is_Cancelled = 0 THEN "Order ID" END) AS Total_Orders,
    SUM(CASE WHEN Is_Cancelled = 0 THEN Qty ELSE 0 END) AS Total_Quantity,
    ROUND(
        SUM(Is_Cancelled) * 100.0 / COUNT(*),
        2
    ) AS Cancellation_Rate_Pct,
    ROUND(
        SUM(CASE WHEN Is_Cancelled = 0 THEN Amount ELSE 0 END) * 1.0 /
        COUNT(DISTINCT CASE WHEN Is_Cancelled = 0 THEN "Order ID" END),
        2
    ) AS Average_Order_Value
FROM amazon_sales;