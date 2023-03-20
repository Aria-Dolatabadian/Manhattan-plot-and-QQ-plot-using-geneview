import matplotlib.pyplot as plt
import geneview as gv
import pandas as pd

# load data
df = pd.read_csv("gwas.csv")
print(df)
# Plot a basic manhattan plot with horizontal xtick labels and the figure will display in screen.
ax = gv.manhattanplot(data=df)
plt.show()

ax = gv.manhattanplot(data=df, xticklabel_kws={"rotation": "vertical"})
plt.show()

ax = gv.manhattanplot(data=df,
                   suggestiveline=None,  # Turn off suggestiveline
                   genomewideline=None,  # Turn off genomewideline
                   xticklabel_kws={"rotation": "vertical"})
plt.show()

# plot only results of chromosome 8.
gv.manhattanplot(data=df, CHR="ChrA08", xlabel="Chromosome 8")
plt.show()

ax = gv.manhattanplot(data=df,
                   sign_marker_p=1e-6,  # highline the significant SNP with ``sign_marker_color`` color.
                   is_annotate_topsnp=True,  # annotate the top SNP
                   xticklabel_kws={"rotation": "vertical"})
plt.show()

ax = gv.qqplot(data=df["P"])
plt.show()
