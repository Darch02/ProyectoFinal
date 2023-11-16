terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "app_server" {
  ami                         = "ami-053b0d53c279acc90"
  instance_type               = "t2.micro"
  key_name                    = "llaveServidorChat"
  vpc_security_group_ids      = ["sg-0822497ac6e45112f"]
  subnet_id                   = "subnet-057f83eec28577b3f"
  associate_public_ip_address = true

  provisioner "file" {
    source      = "proyecto.tar.gz"
    destination = "/home/ubuntu/proyecto.tar.gz"
  }

  provisioner "remote-exec" {
    inline = ["tar -xvf /home/ubuntu/proyecto.tar.gz", "cd /home/ubuntu/proyecto", "sudo apt update","sudo sh script.sh"]
  }

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("~/Documentos/proyecto/llaveServidorChat.pem")
    host        = self.public_ip
  }

  tags = {
    Name = "ServidorChatCarpool"
  }
}
