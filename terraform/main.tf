provider "aws" {
  region = "ap-southeast-2" 
}

resource "aws_instance" "example" {
  ami           = "ami-09eebd0b9bd845bf1" 
  instance_type = "t2.micro"

  tags = {
    Name = "MyTerraformInstance"
  }
}

resource "aws_db_instance" "default" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t2.micro"
  db_name              = "mydatabase"
  username             = "dbuser"
  password             = "yourpassword"
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true

  tags = {
    Name = "MyTerraformRDS"
  }
}
