FROM lambci/lambda:build-python3.7
RUN yum install -y zip
RUN yum clean all
RUN python3.7 -m pip install --upgrade pip
RUN pip install -t /opt/python/ python-Levenshtein==0.12.0
RUN cd /opt; zip -r ../layer.zip *;
RUN echo "/layer.zip is ready";
RUN ls -alh /layer.zip;