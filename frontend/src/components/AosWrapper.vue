<template>
    <div 
        :data-aos="aos"
        :data-aos-delay="delay"
        :data-aos-duration="duration">
        <slot></slot>
    </div>
</template>


<script>
export default {
    props: {
        aos: {
            type: String,
            default:'fade-up'
        },
        delay: {
            type: [String, Number],
            default: 200
        },
        duration: {
            type: [String, Number],
            default: 800
        }
    }
}
</script>