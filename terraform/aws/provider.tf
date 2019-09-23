# Define these as ENV variables
variable "aws_access_key" {}
variable "aws_secret_key" {}

variable "aws_region" {
  default = "us-east-1"	
}

provider "aws" {
  access_key = "${var.aws_access_key}"
  secret_key = "${var.aws_secret_key}"
  region     = "${var.aws_region}"
}

resource "aws_instance" "web_server" {
  ami           = "${lookup(var.webserver_amis, var.aws_region)}"
  instance_type = "t2.micro"
}

