import streamlit as st
import plotly.express as px
import pandas as pd

data = pd.read_csv("Iris.csv")
st.title("Iris Flower Dashboard")
st.divider()
with st.sidebar:
    st.header("Description")
    st.subheader("Nevertheless, all three species of Iris are separable in the projection on the nonlinear and branching principal component.[7] The data set is approximated by the closest tree with some penalty for the excessive number of nodes, bending and stretching. Then the so-called metro map is constructed.[4] The data points are projected into the closest node. For each node the pie diagram of the projected points is prepared. The area of the pie is proportional to the number of the projected points. It is clear from the diagram (left) that the absolute majority of the samples of the different Iris species belong to the different nodes. Only a small fraction of Iris-virginica is mixed with Iris-versicolor (the mixed blue-green nodes in the diagram). Therefore, the three species of Iris (Iris setosa, Iris virginica and Iris versicolor) are separable by the unsupervising procedures of nonlinear principal component analysis. To discriminate them, it is sufficient just to select the corresponding nodes on the principal tree.")
col1,col2=st.columns(2)
with col1:
    st.header("Pie Chart of Species")
    fig_pie = px.pie(data, names = "species",values = "sepal_length", title = "Species of Flower")
    st.plotly_chart(fig_pie, use_container_width=True)
    

with col2:
    st.header("Bar Chart of Species")
    fig_bar = px.bar(data, y = "sepal_width",x = "species", title = "Species of Flower")
    st.plotly_chart(fig_bar, use_container_width=True)


st.divider()

st.header("Line chart of Species")
fig_line = px.line(data, y = ["sepal_length","sepal_width","petal_length","petal_length"],title = "Species of Flower")
st.plotly_chart(fig_line, use_container_width=True)

st.divider()

col1,col2,col3 =st.columns(3)

with col1:
    st.header("Scatter plot of Sepal Length vs Sepal Width")
    fig_pie = px.scatter(data, x = "sepal_length",y = "sepal_width", title = "Species of Flower")
    st.plotly_chart(fig_pie, use_container_width=True)
    

with col2:
    st.header("Bubble chart")
    fig = px.scatter_3d(data, x='sepal_length', y='sepal_width', z='petal_width',color='species')
    st.plotly_chart(fig, use_container_width=True)
with col3:
    st.header("Scatter plot")
    fig_pie = px.scatter(data, x = "petal_length",y = "petal_length", title = "Species of Flower")
    st.plotly_chart(fig_pie, use_container_width=True)
st.divider()
