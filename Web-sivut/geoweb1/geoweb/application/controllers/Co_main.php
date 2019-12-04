<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Co_main extends CI_Controller {
		/**

		*/
	
	
	public function login_index()
	{
		$this->load->view('Pg_login');
	}
	
	public function info_index()
	{
		$this->load->view('Pg_info');
	}
	public function map_index(){
		/**
			tietokantojen käyttöä
		*/
		$this->load->model('User_model');
		$data['userArray'] = $this->User_model->return_users();
		$this->load->view('Pg_map_test',$data);
		
		}
	
}
