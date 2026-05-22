CREATE DATABASE  Transactions_db;
USE Transactions_db;

CREATE TABLE Transactions (
    OrderID VARCHAR(50) NOT NULL,
    Date DATE NOT NULL,
    CustomerID VARCHAR(50) NOT NULL,
    Product VARCHAR(100) NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    ShippingAddress VARCHAR(255),
    PaymentMethod VARCHAR(50),
    OrderStatus VARCHAR(50),
    TrackingNumber VARCHAR(50),
    ItemsInCart INT,
    CouponCode VARCHAR(50),
    ReferralSource VARCHAR(50),
    TotalPrice DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (OrderID)
);

SELECT COUNT(*) FROM Transactions;

-- TASK 1: OVERALL REVENUE AND TRANSACTION VOLUMES
-- Computes baseline organizational health metrics across the data timeline.
SELECT 
    COUNT(OrderID) AS Total_Transactions,
    SUM(TotalPrice) AS Total_Revenue,
    ROUND(AVG(TotalPrice), 2) AS Average_Order_Value,
    ROUND(AVG(ItemsInCart), 2) AS Average_Items_Per_Cart
FROM transactions;

SELECT 
    Product,
    COUNT(OrderID) AS Order_Count,
    SUM(Quantity) AS Total_Units_Sold,
    SUM(TotalPrice) AS Gross_Product_Revenue
FROM Transactions_db.Transactions
GROUP BY Product
ORDER BY Gross_Product_Revenue DESC;

SELECT 
    OrderID,
    CustomerID,
    Product,
    TotalPrice,
    OrderStatus
FROM Transactions_db.Transactions
WHERE TotalPrice > 1500.00
ORDER BY TotalPrice DESC;

SELECT 
    ReferralSource,
    PaymentMethod,
    COUNT(OrderID) AS Conversion_Count,
    SUM(TotalPrice) AS Revenue_By_Channel
FROM Transactions_db.Transactions
GROUP BY ReferralSource, PaymentMethod
ORDER BY Revenue_By_Channel DESC;