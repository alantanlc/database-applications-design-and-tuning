<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
	<html>
		<body>
			<h2>Query C</h2>
			<p>Print the total quantity of items called "Sunscreen" available in Indonesia.</p>
			<xsl:value-of select="sum(//item[name='Sunscreen' and ../../address/country='Indonesia']/qty)" /> 
		</body>
	</html>
</xsl:template>

</xsl:stylesheet>