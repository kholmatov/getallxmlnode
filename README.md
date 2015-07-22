# getallxmlnodexpath
Python script for get all xml node and attribute xpath

Run example in shell:
<pre>Python getnodexpath.py yourxmlfile.xml</pre>

script return JSON array:

<pre>
{
    "attr": [
        "/multivectorautofeed/companies/company/stores/store/descriptions/description/@language",
        "/multivectorautofeed/companies/company/stores/store/addresses/location/@main"
    ],
    "node": [
        "/multivectorautofeed",
        "/multivectorautofeed/general",
        "/multivectorautofeed/general/version",
        "/multivectorautofeed/general/builddate",
        "/multivectorautofeed/general/contentdate",
        "/multivectorautofeed/general/companyname",
        "/multivectorautofeed/companies",
        "/multivectorautofeed/companies/company",
        "/multivectorautofeed/companies/company/companyid",
        "/multivectorautofeed/companies/company/name"
    ]
}
</pre>
* Need install module:  
<pre>lxml for Python 3.x</pre>

