<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Co_map extends CI_Controller {
		/**

		*/
	function index(){
		/**
			tietokantojen käyttöä
		*/
		$this->load->model('User_model');
		$data['userArray'] = $this->User_model->return_users();
		$this->load->view('Pg_map_test',$data);
		
		}
	
	
	
}
?>
