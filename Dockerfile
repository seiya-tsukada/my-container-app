FROM centos

ARG project_dir="/var/app/"

RUN yum -y install python-devel python-setuptools
RUN easy_install pip

# Create Project Directory
RUN mkdir ${project_dir}
 
# ADD
ADD ./main.py ${project_dir}
ADD ./requirements.txt ${project_dir}

WORKDIR ${project_dir}

RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]