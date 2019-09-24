FROM ubuntu:18.04
MAINTAINER Yuichi Shiraishi <friend1ws@gmail.com> 

RUN apt-get update && apt-get install -y \
    git \
    wget \
    bzip2 \
    make \
    gcc \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    python \
    python3 \
    python3-pip

RUN wget https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2 && \
    tar jxvf htslib-1.9.tar.bz2 && \
    cd htslib-1.9 && \
    make && \
    make install

RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.29.0/bedtools-2.29.0.tar.gz && \
    tar -zxvf bedtools-2.29.0.tar.gz && \
    cd bedtools2 && make && make install

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

RUN pip3 install annot_utils==0.3.0
RUN pip3 install pysam==0.15.2
RUN pip3 install genomon-expression==0.5.0
