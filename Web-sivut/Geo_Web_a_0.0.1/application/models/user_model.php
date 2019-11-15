<?php

	class User_Model extends CI_Model{
		function return_users(){
		$this->load->database();

		$query = $this->db->query("SELECT * FROM gps");
		
		$query->result_array();
		
		return $query->result_array();
		}


	}


?>