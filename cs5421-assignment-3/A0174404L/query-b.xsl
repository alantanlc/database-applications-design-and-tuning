<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
	<html>
		<body>
			<h2>Query B</h2>
			<p>For each warehouse in Singapore or Malaysia, display the name of the warehouse and the name of the items available in the largest quantity in the warehouse.</p>
			<xsl:apply-templates />
		</body>
	</html>
</xsl:template>

<xsl:template match="warehouses">
	<xsl:apply-templates select="warehouse[address/country='Singapore' or address/country='Malaysia']" />
</xsl:template>

<xsl:template match="warehouse[address/country='Singapore' or address/country='Malaysia']">
	<p>
		Warehouse name: <xsl:value-of select="name" /><br/>
		Country: <xsl:value-of select="address/country" /><br/>
		<xsl:apply-templates select="items" />
	</p>
</xsl:template>

<xsl:template match="items">
	<xsl:apply-templates select="item[not(../item/qty > qty)]" />
</xsl:template>

<xsl:template match="item">
	Item name: <xsl:value-of select="name" />, Quantity: <xsl:value-of select="qty" /><br />
</xsl:template>

</xsl:stylesheet>