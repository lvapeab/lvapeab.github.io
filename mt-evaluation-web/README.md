# Machine translation human evaluation

This website provides tools for performing the [Direct Assessment (DA) protocol]() for evaluating translation hypotheses.



## Usage

You should provide two files, one with machine translation hypotheses and another one with the corresponding reference translations.<br>


Each file must contain a line per sentence, with the following format:

`#block \t sys \t domain \t #sentence \t sentence`

were:
<ul style="list-style-type: none">
            <li><code>#block</code> &rarr;  block identifier. </li>
            <li><code>\t</code> &rarr;  tabular symbol.</li>
            <li><code>sys</code> &rarr; system identifier.</li>
            <li><code>domain</code> &rarr; domain identifier.</li>
            <li><code>#sentence</code> &rarr;  sentence identifier.</li>
            <li><code>sentence</code> &rarr; sentence to be displayed.</li>
</ul>


## Related research

This website has been developed for and used in the following work:


[Are Automatic Metrics Robust and Reliable in Specific Machine Translation Tasks?](mt-evaluation-web/resources/eamt18.pdf). Mara Chinea-Rios, Álvaro Peris, and Francisco Casacuberta. In <em> Proceedings of the 21st Annual Conference of the European Association for Machine Translation, pp. 89-98</em>, 2018.

### Data

The data used in these paper are available at [mt-evaluation-web/resources/eamt18_data.zip](mt-evaluation-web/resources/eamt18_data.zip)            </ul>


### Citation

If you use the data or the website for academic purposes, please cite the following work:
```
    @inproceedings{Chinea18,
      title= {Are Automatic Metrics Robust and Reliable in Specific Machine Translation Tasks?},
      author= {Chinea-Rios, Mara and Peris, Alvaro and Casacuberta, Francisco},
      booktitle= {Proceedings of the 21st Annual Conference of the European Association for Machine Translation},
      year      = {2018},  
      pages= {89--98}
}
```




## Contact

Álvaro Peris ([web page](http://lvapeab.github.io/)): lvapeab@prhlt.upv.es 

