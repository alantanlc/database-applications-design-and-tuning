<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
	<html>
		<body>
			<h2>Query A</h2>
			<p>For each warehouse in Singapore, list the items that are available in the warehouse in quantity larger than 975. Print the name of each warehouse followed by the list of the names of the items it contains and the quantity available.</p>
			<xsl:apply-templates />
		</body>
	</html>
</xsl:template>

<xsl:template match="warehouses">
	<xsl:apply-templates select="warehouse[address/country='Singapore']" />
</xsl:template>

<xsl:template match="warehouse[address/country='Singapore']">
	<p>
		Warehouse name: <xsl:value-of select="name" /><br/>
		Country: <xsl:value-of select="address/country" /><br/>
		<xsl:apply-templates select="items" />
	</p>
</xsl:template>

<xsl:template match="items">
	<xsl:apply-templates select="item[qty>975]" />
</xsl:template>

<xsl:template match="item">
	Item name: <xsl:value-of select="name" />, Quantity: <xsl:value-of select="qty" /><br />
</xsl:template>

</xsl:stylesheet>