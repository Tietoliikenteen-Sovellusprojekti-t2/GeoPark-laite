<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Co_main extends CI_Controller {
		/**
		*/

	
	public function index()
	{
		$this->load->view('Pg_main');
	}
	public function video()
	{
		$this->load->view('Pg_video');
	}
	
	public function info()
	{
		$this->load->view('Pg_info');
	}
	public function map(){
		/**
			tietokantojen käyttöä
		*/
		$this->load->model('User_model');
		$data['userArray'] = $this->User_model->return_users();
		$this->load->view('Pg_map',$data);
		
		}
	
}
