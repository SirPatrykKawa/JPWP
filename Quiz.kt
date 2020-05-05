package com.chudy.jpwplab3.model

data class Quiz(val id: Int, val name:String, val publish_at:String, val answers:List<Answer>)